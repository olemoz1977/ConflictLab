# ConflictLab — Hostinger Processor Review

**Review date:** 2026-08-15  
**Status:** SUFFICIENT FOR TECHNICAL LAB / final live-account verification remains before CALIBRATION activation  
**Controller:** Oleg Mozochin  
**Service context:** OMESG360 / ConflictLab on Hostinger Premium Web Hosting

## 1. Owner-verified service facts

Owner screenshots on 2026-08-15 establish for the current `omesg360.eu` hosting plan:

```text
plan: Premium Web Hosting
primary server location: Europe (Lithuania)
backup location: France
backup cadence shown in hPanel: weekly
SSL: active
CDN: active
hPanel analytics: server/access-log based
```

These facts are specific to the owner account and must be rechecked if the hosting plan/location changes.

## 2. Hostinger DPA status

Current official Hostinger Data Processing Addendum reviewed on 2026-08-15; the published page reports revision date 2026-07-14.

The DPA states that for Customer Data processed within Covered Services:

- Hostinger acts as Processor and the Customer acts as Controller or Processor as applicable;
- Hostinger processes Customer Data to provide Covered Services and documented customer instructions;
- Hostinger offers controls/assistance relevant to data-subject access, correction, deletion or restriction;
- Hostinger may use authorized sub-processors under written obligations and remains responsible for DPA compliance;
- new sub-processors are added to Appendix 3 and the customer has the contractual objection/termination mechanism described in the DPA;
- transfers outside the EEA to countries without adequacy may be governed by the EU Standard Contractual Clauses described in the DPA;
- Hostinger's security model remains shared: the customer is responsible for correct configuration, access control and appropriate deletion/security use of the service.

Reference:

```text
Hostinger Data Processing Addendum
https://www.hostinger.com/lt/legal/dpa
reviewed: 2026-08-15
published revision shown: 2026-07-14
```

The English legal version should be treated as controlling if Hostinger's translated text conflicts with it.

## 3. Authorized sub-processor register

Appendix 3 of the DPA currently lists:

```text
AMAZON WEB SERVICES EMEA SARL
Google Cloud EMEA Limited
Cloudflare, Inc.
MailChannels Corporation
Proofpoint, Inc.
Anthropic Ireland, Limited
spectra tech, UAB
```

Interpretation boundary:

> This is Hostinger's authorized DPA list. It is NOT evidence that every listed sub-processor receives ConflictLab timing records in this specific hosting configuration.

ConflictLab will not assert a specific per-record transfer route unless Hostinger provides service-specific evidence.

## 4. International-transfer position

Owner-verified primary storage and backup locations are within the EEA:

```text
Lithuania
France
```

However, Hostinger's global service/support/sub-processor architecture may still involve Customer Data processing or onward transfer outside the EEA depending on the Covered Service.

The DPA states that relevant non-adequate-country transfers are covered by its EU SCC framework.

Therefore participant-facing wording should not claim:

```text
"your data never leave the EEA"
```

A defensible wording is:

> Primary hosting and backups for the current plan are configured in Lithuania and France. Where Hostinger or an authorized sub-processor processes Customer Data outside the EEA, applicable transfer safeguards described in Hostinger's DPA apply.

## 5. Backup retention

Official Hostinger help documentation reviewed 2026-08-15 states for web/cloud hosting:

```text
weekly backups: retained for 6 weeks
daily backups: retained for 7 days (where enabled)
```

The owner account shows weekly backups on the current Premium Web Hosting plan.

Therefore the current operational assumption is:

```text
active calibration DB record retention: max 90 days
Hostinger weekly backup rotation: up to 6 weeks
```

This creates an important deletion distinction.

### Active-system deletion

Participant deletion code / retention cleanup can delete:

```text
cl_calibration_pair_events
cl_calibration_attempts
cl_calibration_runs
```

from the active calibration database immediately when the deletion operation succeeds.

### Backup copies

A deleted active record may remain inside an already-created Hostinger backup until that backup leaves the provider's normal rotation.

The participant notice must therefore not promise that all physical backup copies disappear instantly.

Preferred disclosure:

> Deletion removes the record from the active ConflictLab research database. Residual copies may remain temporarily in Hostinger's protected backup rotation and expire according to the hosting backup lifecycle. They are not used for research analysis. If a backup restoration reintroduces an already-deleted active record, the deletion must be re-applied where technically identifiable.

This disclosure must be aligned with the actually verified Hostinger backup behavior at activation time.

## 6. Research use of access/security logs

Hostinger hPanel analytics is derived from server/access logs and can include information such as requests, IP-derived country and IP-address views.

ConflictLab boundary remains:

```text
HOSTINGER ACCESS/SECURITY LOGS
!= CALIBRATION RESEARCH DATASET
```

Do not join access/security logs to timing research data for construct or participant analysis.

## 7. DPA evidence retention

For complaint-readiness, retain an internal dated reference to the DPA version/page reviewed for each activated research phase.

Minimum activation record:

```text
DPA URL
review date
DPA displayed revision date
sub-processor list snapshot/reference
primary server location
backup location
backup cadence/retention
```

Do not copy Hostinger's entire legal text into the project as if ConflictLab controls its future wording. Record the reviewed version/date and re-check the live official source before a new material research phase.

## 8. Remaining processor-related activation tasks

```text
PASS  controller/processor relationship documented
PASS  current DPA reviewed
PASS  authorized sub-processor register reviewed
PASS  SCC transfer mechanism identified
PASS  primary server location verified
PASS  backup location verified
PASS  weekly backup lifecycle identified from Hostinger documentation
OPEN  confirm the live account still shows weekly backup status immediately before CALIBRATION activation
OPEN  update final active participant notice with backup-rotation deletion qualification
OPEN  include processor review date in CALIBRATION_ACTIVATION_RECORD_v0.1
```

No new screenshot is required now unless the plan, server region or backup configuration changes before activation.
