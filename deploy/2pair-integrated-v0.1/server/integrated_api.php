<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

const MAX_BODY_BYTES = 196608;
const BLOCK_SCHEMA = '2pair.integrated.block.v0.1';
const REFLECTION_SCHEMA = '2pair.integrated.reflection.v0.1';
const ALLOWED_RUN_TYPES = ['TECHNICAL','RESEARCH'];
const ALLOWED_LANGUAGES = ['lt','en'];
const ALLOWED_DEVICE_CATEGORIES = ['mobile','tablet','desktop','unknown'];
const ALLOWED_FORMS = [
    'F2-A' => ['CS-CA-01','CR-PZ-01','CR-PO-01'],
    'F2-B' => ['CS-PR-01','CS-RE-01','CR-FS-01'],
];
const PAIRS = [
    'CS-PR-01' => ['A'=>'CS-PR-01-A','B'=>'CS-PR-01-B'],
    'CS-RE-01' => ['A'=>'CS-RE-01-A','B'=>'CS-RE-01-B'],
    'CS-CA-01' => ['A'=>'CS-CA-01-A','B'=>'CS-CA-01-B'],
    'CR-PZ-01' => ['A'=>'CR-PZ-01-A','B'=>'CR-PZ-01-B'],
    'CR-FS-01' => ['A'=>'CR-FS-01-A','B'=>'CR-FS-01-B'],
    'CR-PO-01' => ['A'=>'CR-PO-01-A','B'=>'CR-PO-01-B'],
];

function respond(int $status, array $payload): never {
    http_response_code($status);
    echo json_encode($payload, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
    exit;
}
function fail(int $status, string $code, string $message): never {
    respond($status, ['ok'=>false,'code'=>$code,'message'=>$message]);
}
function is_uuid(string $value): bool {
    return preg_match('/^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i', $value) === 1;
}
function is_sha256_hex(string $value): bool {
    return preg_match('/^[0-9a-f]{64}$/', $value) === 1;
}
function require_string(array $src, string $key, int $max=128): string {
    $v=$src[$key]??null;
    if(!is_string($v)||$v===''||strlen($v)>$max) fail(422,'INVALID_FIELD',"$key is invalid");
    return $v;
}
function require_int(array $src,string $key,int $min,int $max): int {
    $v=$src[$key]??null;
    if(!is_int($v)||$v<$min||$v>$max) fail(422,'INVALID_FIELD',"$key is invalid");
    return $v;
}
function require_bool(array $src,string $key): bool {
    $v=$src[$key]??null;
    if(!is_bool($v)) fail(422,'INVALID_FIELD',"$key is invalid");
    return $v;
}
function nullable_int(array $src,string $key,int $min,int $max): ?int {
    if(!array_key_exists($key,$src)||$src[$key]===null)return null;
    return require_int($src,$key,$min,$max);
}
function nullable_text(array $src,string $key,int $maxChars=2000): ?string {
    if(!array_key_exists($key,$src)||$src[$key]===null)return null;
    if(!is_string($src[$key])) fail(422,'INVALID_FIELD',"$key is invalid");
    $v=trim($src[$key]); if($v==='')return null;
    return mb_substr($v,0,$maxChars);
}
function db(array $config): PDO {
    return new PDO((string)$config['db']['dsn'],(string)$config['db']['user'],(string)$config['db']['password'],[
        PDO::ATTR_ERRMODE=>PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE=>PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES=>false,
    ]);
}
function validate_common(array $payload,array $config,string $runType): array {
    $sessionUuid=require_string($payload,'sessionId',36);
    $releaseId=require_string($payload,'releaseId',64);
    $protocolVersion=require_string($payload,'protocolVersion',64);
    $stimulusSetVersion=require_string($payload,'stimulusSetVersion',64);
    $trainingSetVersion=require_string($payload,'trainingSetVersion',64);
    $language=require_string($payload,'language',2);
    $deviceCategory=require_string($payload,'deviceCategory',16);
    if(!is_uuid($sessionUuid)) fail(422,'INVALID_UUID','sessionId must be UUID');
    if($releaseId!==($config['release_id']??null)) fail(422,'RELEASE_MISMATCH','unexpected release');
    if($protocolVersion!==($config['protocol_version']??null)) fail(422,'PROTOCOL_MISMATCH','unexpected protocol');
    if($stimulusSetVersion!==($config['stimulus_set_version']??null)) fail(422,'STIMULUS_SET_MISMATCH','unexpected stimulus set');
    if($trainingSetVersion!==($config['training_set_version']??null)) fail(422,'TRAINING_SET_MISMATCH','unexpected training set');
    if(!in_array($language,ALLOWED_LANGUAGES,true)) fail(422,'INVALID_LANGUAGE','unsupported language');
    if(!in_array($deviceCategory,ALLOWED_DEVICE_CATEGORIES,true)) fail(422,'INVALID_DEVICE_CATEGORY','unsupported device category');

    $consentVersion=null;$researchConsent=null;$age18Confirmed=null;$deletionTokenHash=null;
    $hasConsent=array_key_exists('consentVersion',$payload)||array_key_exists('researchConsent',$payload)||array_key_exists('age18Confirmed',$payload)||array_key_exists('deletionTokenHash',$payload);
    if($runType==='RESEARCH'||$hasConsent){
        $consentVersion=require_string($payload,'consentVersion',64);
        $researchConsent=require_bool($payload,'researchConsent');
        $age18Confirmed=require_bool($payload,'age18Confirmed');
        $deletionTokenHash=require_string($payload,'deletionTokenHash',64);
        if(!is_sha256_hex($deletionTokenHash)) fail(422,'INVALID_DELETION_TOKEN_HASH','deletionTokenHash must be lowercase SHA-256 hex');
    }
    if($runType==='RESEARCH'){
        if($consentVersion!==(string)($config['consent_version']??'')) fail(422,'CONSENT_VERSION_MISMATCH','unexpected consent version');
        if($researchConsent!==true) fail(422,'RESEARCH_CONSENT_REQUIRED','affirmative research consent required');
        if($age18Confirmed!==true) fail(422,'AGE_CONFIRMATION_REQUIRED','18+ confirmation required');
    }
    return compact('sessionUuid','releaseId','protocolVersion','stimulusSetVersion','trainingSetVersion','language','deviceCategory','consentVersion','researchConsent','age18Confirmed','deletionTokenHash');
}
function get_or_create_session(PDO $pdo,array $common,string $runType): int {
    $q=$pdo->prepare('SELECT * FROM tp_integrated_sessions WHERE session_uuid=? LIMIT 1');
    $q->execute([$common['sessionUuid']]); $row=$q->fetch();
    if($row){
        $checks=[
            'release_id'=>$common['releaseId'],'run_type'=>$runType,'protocol_version'=>$common['protocolVersion'],
            'stimulus_set_version'=>$common['stimulusSetVersion'],'training_set_version'=>$common['trainingSetVersion'],
            'language'=>$common['language'],'device_category'=>$common['deviceCategory'],
        ];
        foreach($checks as $k=>$v) if((string)$row[$k]!== (string)$v) fail(409,'SESSION_PROVENANCE_MISMATCH','existing session provenance differs');
        if($runType==='RESEARCH'){
            if((string)$row['consent_version']!==(string)$common['consentVersion']||(int)$row['research_consent']!==1||(int)$row['age_18_confirmed']!==1||(string)$row['deletion_token_hash']!==(string)$common['deletionTokenHash'])
                fail(409,'SESSION_CONSENT_MISMATCH','existing session consent differs');
        }
        return (int)$row['id'];
    }
    $ins=$pdo->prepare('INSERT INTO tp_integrated_sessions (session_uuid,release_id,run_type,protocol_version,stimulus_set_version,training_set_version,language,device_category,consent_version,research_consent,age_18_confirmed,deletion_token_hash) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)');
    $ins->execute([$common['sessionUuid'],$common['releaseId'],$runType,$common['protocolVersion'],$common['stimulusSetVersion'],$common['trainingSetVersion'],$common['language'],$common['deviceCategory'],$common['consentVersion'],$common['researchConsent']===null?null:($common['researchConsent']?1:0),$common['age18Confirmed']===null?null:($common['age18Confirmed']?1:0),$common['deletionTokenHash']]);
    return (int)$pdo->lastInsertId();
}

if($_SERVER['REQUEST_METHOD']!=='POST'){header('Allow: POST');fail(405,'METHOD_NOT_ALLOWED','POST required');}
$contentType=strtolower((string)($_SERVER['CONTENT_TYPE']??''));
if(!str_starts_with($contentType,'application/json')) fail(415,'UNSUPPORTED_MEDIA_TYPE','application/json required');
$raw=file_get_contents('php://input'); if($raw===false||$raw==='')fail(400,'EMPTY_BODY','JSON body required'); if(strlen($raw)>MAX_BODY_BYTES)fail(413,'PAYLOAD_TOO_LARGE','payload too large');
try{$payload=json_decode($raw,true,64,JSON_THROW_ON_ERROR);}catch(JsonException $e){fail(400,'INVALID_JSON','invalid JSON');}
if(!is_array($payload))fail(400,'INVALID_JSON','JSON object required');
$configPath=__DIR__.'/config.php'; if(!is_file($configPath))fail(503,'SERVER_NOT_CONFIGURED','server is not configured');
$config=require $configPath; if(!is_array($config)||!isset($config['db']))fail(503,'SERVER_NOT_CONFIGURED','invalid server config');
$runType=strtoupper((string)($config['collection_mode']??'TECHNICAL')); if(!in_array($runType,ALLOWED_RUN_TYPES,true))fail(503,'SERVER_NOT_CONFIGURED','invalid collection mode');
$schema=require_string($payload,'schema',64);
$common=validate_common($payload,$config,$runType);

if($schema===BLOCK_SCHEMA){
    $messageId=require_string($payload,'messageId',36); if(!is_uuid($messageId))fail(422,'INVALID_UUID','messageId must be UUID');
    $block=$payload['block']??null; if(!is_array($block))fail(422,'INVALID_BLOCK','block object required');
    $blockUuid=require_string($block,'blockId',36); if(!is_uuid($blockUuid))fail(422,'INVALID_UUID','blockId must be UUID');
    $blockIndex=require_int($block,'blockIndex',1,2); $formId=require_string($block,'formId',16); if(!isset(ALLOWED_FORMS[$formId]))fail(422,'INVALID_FORM','unknown form');
    $budget=require_int($block,'blockBudgetMs',1,60000); if($budget!==(int)($config['block_budget_ms']??0))fail(422,'BUDGET_MISMATCH','unexpected block budget');
    $preload=require_bool($block,'technicalPreloadOk'); if(!$preload)fail(422,'PRELOAD_NOT_CONFIRMED','block requires successful preload');
    $attempts=$block['attempts']??null;$events=$block['events']??null;
    if(!is_array($attempts)||count($attempts)<1||count($attempts)>3)fail(422,'INVALID_ATTEMPTS','1..3 attempts required');
    if(!is_array($events)||count($events)!==count($attempts)*3)fail(422,'INVALID_EVENTS','three logical events per attempt required');

    $attemptByNumber=[];
    foreach($attempts as $a){
        if(!is_array($a))fail(422,'INVALID_ATTEMPT','attempt object required');
        $attemptUuid=require_string($a,'blockAttemptId',36);if(!is_uuid($attemptUuid))fail(422,'INVALID_UUID','blockAttemptId must be UUID');
        $n=require_int($a,'blockAttemptNumber',1,3);if(isset($attemptByNumber[$n]))fail(422,'DUPLICATE_ATTEMPT','duplicate attempt number');
        $ab=require_int($a,'blockBudgetMs',1,60000);$elapsed=require_int($a,'blockElapsedMsFinal',0,$budget);$timed=require_bool($a,'blockTimedOut');$hidden=require_bool($a,'pageHiddenDuringBlock');
        $isTraining=require_bool($a,'isTraining');$pv=require_string($a,'protocolVersion',64);$sv=require_string($a,'stimulusSetVersion',64);
        if($ab!==$budget||$isTraining||$pv!==$common['protocolVersion']||$sv!==$common['stimulusSetVersion'])fail(422,'ATTEMPT_BOUNDARY_MISMATCH','attempt violates integrated boundary');
        $attemptByNumber[$n]=['uuid'=>$attemptUuid,'number'=>$n,'elapsed'=>$elapsed,'timed'=>$timed,'hidden'=>$hidden];
    }
    ksort($attemptByNumber);if(array_keys($attemptByNumber)!==range(1,count($attempts)))fail(422,'ATTEMPT_SEQUENCE','attempts must start at 1');

    $eventsByAttempt=[];$seen=[];
    foreach($events as $e){
        if(!is_array($e))fail(422,'INVALID_EVENT','event object required');
        $eventUuid=require_string($e,'eventId',36);if(!is_uuid($eventUuid)||isset($seen[$eventUuid]))fail(422,'INVALID_EVENT_ID','event UUID invalid or duplicate');$seen[$eventUuid]=true;
        $n=require_int($e,'blockAttemptNumber',1,3);$attemptUuid=require_string($e,'blockAttemptId',36);if(!isset($attemptByNumber[$n])||$attemptByNumber[$n]['uuid']!==$attemptUuid)fail(422,'EVENT_ATTEMPT_MISMATCH','event attempt mismatch');
        $pairId=require_string($e,'pairId',32);if(!in_array($pairId,ALLOWED_FORMS[$formId],true))fail(422,'PAIR_FORM_MISMATCH','pair not in selected form');
        $pos=require_int($e,'positionInBlock',1,3);$global=require_int($e,'sessionPresentationIndex',1,6);$expectedGlobal=($blockIndex-1)*3+$pos;if($global!==$expectedGlobal)fail(422,'PRESENTATION_INDEX_MISMATCH','session presentation index mismatch');
        $presented=require_bool($e,'pairPresented');$exposure=nullable_int($e,'pairExposureNumber',1,20);$ready=nullable_int($e,'pairReadyElapsedMs',0,$budget);$choice=require_string($e,'choice',24);$latency=nullable_int($e,'visualChoiceLatencyMs',0,$budget);$elapsed=require_int($e,'blockElapsedMsAtEvent',0,$budget);$remaining=nullable_int($e,'remainingBudgetAtPairStartMs',0,$budget);$hiddenBefore=require_bool($e,'pageHiddenBeforeEvent');
        $assetA=require_string($e,'assetAId',32);$assetB=require_string($e,'assetBId',32);$aPos=require_string($e,'assetAPosition',8);$bPos=require_string($e,'assetBPosition',8);
        if($assetA!==PAIRS[$pairId]['A']||$assetB!==PAIRS[$pairId]['B'])fail(422,'ASSET_ID_MISMATCH','unexpected asset identity');
        if(!in_array($aPos,['top','bottom'],true)||!in_array($bPos,['top','bottom'],true)||$aPos===$bPos)fail(422,'POSITION_INVALID','asset positions invalid');
        if(!in_array($choice,['A','B','no_clear_choice','timeout'],true))fail(422,'INVALID_CHOICE','unsupported choice');
        if(!$presented&&$exposure!==null)fail(422,'UNPRESENTED_EXPOSURE','unpresented event cannot have exposure number');
        if($presented&&$exposure===null)fail(422,'PRESENTED_EXPOSURE_REQUIRED','presented event requires exposure number');
        if($choice==='timeout'){
            if($latency!==null)fail(422,'TIMEOUT_LATENCY','timeout cannot have latency');
            if(!$presented&&($ready!==null||$remaining!==null))fail(422,'UNPRESENTED_TIMING','unpresented timeout cannot have ready timing');
        }else{
            if(!$presented||$ready===null||$remaining===null||$latency===null)fail(422,'RESPONSE_TIMING_INCOMPLETE','completed response requires timing');
        }
        $eventsByAttempt[$n][]=['uuid'=>$eventUuid,'attemptUuid'=>$attemptUuid,'attemptNumber'=>$n,'pairId'=>$pairId,'position'=>$pos,'global'=>$global,'presented'=>$presented,'exposure'=>$exposure,'ready'=>$ready,'assetA'=>$assetA,'assetB'=>$assetB,'aPos'=>$aPos,'bPos'=>$bPos,'choice'=>$choice,'latency'=>$latency,'elapsed'=>$elapsed,'remaining'=>$remaining,'hiddenBefore'=>$hiddenBefore];
    }
    foreach($attemptByNumber as $n=>$_){$group=$eventsByAttempt[$n]??[];if(count($group)!==3)fail(422,'EVENT_COUNT_PER_ATTEMPT','three events required');$positions=array_map(fn($x)=>$x['position'],$group);sort($positions);if($positions!==[1,2,3])fail(422,'POSITION_SET','positions must be 1,2,3');$pairs=array_map(fn($x)=>$x['pairId'],$group);sort($pairs);$exp=ALLOWED_FORMS[$formId];sort($exp);if($pairs!==$exp)fail(422,'PAIR_SET','attempt pair set mismatch');}
    $primary=$attemptByNumber[1];$cleanPrimary=!$primary['hidden'];$exclusion=$cleanPrimary?null:'PAGE_HIDDEN_DURING_PRIMARY';

    try{$pdo=db($config);
        $idempotent=$pdo->prepare('SELECT id FROM tp_integrated_blocks WHERE message_id=? LIMIT 1');$idempotent->execute([$messageId]);if($idempotent->fetch())respond(200,['ok'=>true,'idempotent'=>true]);
        $pdo->beginTransaction();$sessionDbId=get_or_create_session($pdo,$common,$runType);
        $existing=$pdo->prepare('SELECT block_index,form_id FROM tp_integrated_blocks WHERE session_id=? FOR UPDATE');$existing->execute([$sessionDbId]);$existingBlocks=$existing->fetchAll();
        foreach($existingBlocks as $b){if((int)$b['block_index']===$blockIndex)fail(409,'BLOCK_ALREADY_STORED','block index already stored');if((string)$b['form_id']===$formId)fail(409,'FORM_ALREADY_USED','form already stored');}
        if($blockIndex===2&&count($existingBlocks)!==1)fail(409,'BLOCK_ORDER','block 1 must be stored before block 2');
        if($blockIndex===1&&count($existingBlocks)!==0)fail(409,'BLOCK_ORDER','block 1 must be first');
        if(count($existingBlocks)===1){$other=(string)$existingBlocks[0]['form_id'];if(($other==='F2-A'&&$formId!=='F2-B')||($other==='F2-B'&&$formId!=='F2-A'))fail(409,'FORMS_NOT_COMPLEMENTARY','second form must be complementary');}
        $insB=$pdo->prepare('INSERT INTO tp_integrated_blocks (session_id,message_id,block_uuid,block_index,form_id,block_budget_ms,technical_preload_ok,clean_primary,exclusion_reason) VALUES (?,?,?,?,?,?,?,?,?)');
        $insB->execute([$sessionDbId,$messageId,$blockUuid,$blockIndex,$formId,$budget,1,$cleanPrimary?1:0,$exclusion]);$blockDbId=(int)$pdo->lastInsertId();
        $attemptDbIds=[];$insA=$pdo->prepare('INSERT INTO tp_integrated_attempts (block_id,block_attempt_uuid,attempt_number,block_elapsed_ms_final,block_timed_out,page_hidden_during_block) VALUES (?,?,?,?,?,?)');
        foreach($attemptByNumber as $n=>$a){$insA->execute([$blockDbId,$a['uuid'],$n,$a['elapsed'],$a['timed']?1:0,$a['hidden']?1:0]);$attemptDbIds[$n]=(int)$pdo->lastInsertId();}
        $insE=$pdo->prepare('INSERT INTO tp_integrated_pair_events (block_id,attempt_id,event_uuid,attempt_number,pair_id,position_in_block,session_presentation_index,pair_presented,pair_exposure_number,pair_ready_elapsed_ms,asset_a_id,asset_b_id,asset_a_position,asset_b_position,choice_identity,visual_choice_latency_ms,block_elapsed_ms_at_event,remaining_budget_at_pair_start_ms,page_hidden_before_event) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)');
        foreach($eventsByAttempt as $n=>$group)foreach($group as $e)$insE->execute([$blockDbId,$attemptDbIds[$n],$e['uuid'],$n,$e['pairId'],$e['position'],$e['global'],$e['presented']?1:0,$e['exposure'],$e['ready'],$e['assetA'],$e['assetB'],$e['aPos'],$e['bPos'],$e['choice'],$e['latency'],$e['elapsed'],$e['remaining'],$e['hiddenBefore']?1:0]);
        $pdo->commit();respond(200,['ok'=>true,'idempotent'=>false,'blockIndex'=>$blockIndex,'runType'=>$runType]);
    }catch(PDOException $e){if(isset($pdo)&&$pdo->inTransaction())$pdo->rollBack();error_log('2Pair integrated block API DB error: '.$e->getMessage());fail(500,'DB_ERROR','database error');}
}

if($schema===REFLECTION_SCHEMA){
    $messageId=require_string($payload,'messageId',36);if(!is_uuid($messageId))fail(422,'INVALID_UUID','messageId must be UUID');
    $pairId=require_string($payload,'pairId',32);if(!isset(PAIRS[$pairId]))fail(422,'INVALID_PAIR','unknown pair');
    $anchorEventId=require_string($payload,'anchorEventId',36);if(!is_uuid($anchorEventId))fail(422,'INVALID_UUID','anchorEventId must be UUID');
    $freeText=nullable_text($payload,'freeText',2000);$hard=require_bool($payload,'hardToIdentify');$intensity=nullable_int($payload,'intensity',1,5);
    if($hard)$freeText=null;
    try{$pdo=db($config);
        $idem=$pdo->prepare('SELECT id FROM tp_integrated_reflections WHERE message_id=? LIMIT 1');$idem->execute([$messageId]);if($idem->fetch())respond(200,['ok'=>true,'idempotent'=>true]);
        $s=$pdo->prepare('SELECT * FROM tp_integrated_sessions WHERE session_uuid=? LIMIT 1');$s->execute([$common['sessionUuid']]);$session=$s->fetch();if(!$session)fail(409,'SESSION_NOT_FOUND','store a measured block before reflection');
        if((string)$session['run_type']!==$runType||(string)$session['protocol_version']!==$common['protocolVersion'])fail(409,'SESSION_PROVENANCE_MISMATCH','session provenance differs');
        $q=$pdo->prepare('SELECT e.id,e.choice_identity,e.pair_id,e.attempt_number,b.session_id FROM tp_integrated_pair_events e JOIN tp_integrated_blocks b ON b.id=e.block_id WHERE e.event_uuid=? LIMIT 1');$q->execute([$anchorEventId]);$anchor=$q->fetch();
        if(!$anchor||(int)$anchor['session_id']!==(int)$session['id']||(string)$anchor['pair_id']!==$pairId)fail(422,'ANCHOR_MISMATCH','reflection anchor does not match session/pair');
        if((int)$anchor['attempt_number']!==1)fail(422,'RETRY_REFLECTION_NOT_RESEARCH','only primary-attempt reflection is stored for Wave 1 analysis');
        $choice=(string)$anchor['choice_identity'];if(!in_array($choice,['A','B','no_clear_choice'],true))fail(422,'ANCHOR_NOT_RESPONSE','reflection anchor is not a completed response');
        if($choice==='no_clear_choice'&&$intensity!==null)fail(422,'NCC_INTENSITY','no_clear_choice has no intensity');
        $ins=$pdo->prepare('INSERT INTO tp_integrated_reflections (session_id,pair_event_id,message_id,pair_id,free_text,intensity,hard_to_identify) VALUES (?,?,?,?,?,?,?)');
        $ins->execute([(int)$session['id'],(int)$anchor['id'],$messageId,$pairId,$freeText,$intensity,$hard?1:0]);respond(200,['ok'=>true,'idempotent'=>false]);
    }catch(PDOException $e){if($e->getCode()==='23000')fail(409,'REFLECTION_ALREADY_STORED','reflection already stored for this pair');error_log('2Pair integrated reflection API DB error: '.$e->getMessage());fail(500,'DB_ERROR','database error');}
}

fail(422,'SCHEMA_MISMATCH','unsupported schema');
