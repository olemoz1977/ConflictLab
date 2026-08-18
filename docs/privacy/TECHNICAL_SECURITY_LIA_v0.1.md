# ConflictLab — Technical / Security Legitimate Interests Assessment v0.1

**Date:** 2026-08-15  
**Controller:** Oleg Mozochin  
**Scope:** narrowly necessary OMESG360 / ConflictLab website and server operation, security, abuse prevention, integrity and technical troubleshooting.  
**Explicit exclusion:** this LIA does **not** provide the legal basis for optional timing research. Timing research uses separate opt-in consent.

## 1. Processing considered

This LIA covers technical processing that may occur when a person accesses OMESG360 / ConflictLab infrastructure, including provider/server access and security logs such as:

```text
IP address
request time
requested resource / HTTP request metadata
User-Agent-derived browser/device information
IP-derived country
response/error/security information
```

The Hostinger hPanel Analytics view is based on automatically generated server access logs.

This LIA does not authorize joining these logs to the ConflictLab timing research database for participant or psychological analysis.

## 2. Legal-interest test used

The assessment follows the cumulative Article 6(1)(f) structure described by the EDPB:

```text
1. legitimate interest exists
2. processing is necessary for that interest
3. balancing: data-subject rights/interests do not override it
```

GDPR Recital 49 specifically recognizes processing that is strictly necessary and proportionate for network and information security as a potential legitimate interest.

## 3. Purpose test

### Interest

The controller has a real and present interest in:

- keeping the website and research infrastructure available;
- detecting unauthorized access, malicious requests and abuse;
- diagnosing 4xx/5xx and operational failures;
- investigating security incidents;
- protecting database/admin integrity;
- verifying that technical requests and releases function as intended.

### Conclusion

```text
PURPOSE TEST = PASS FOR NARROW SECURITY/OPERATIONAL SCOPE
```

The interest is lawful, specific and current.

This result does not extend to marketing analytics, behavioural advertising, psychological profiling or optional research telemetry.

## 4. Necessity test

### Why some technical request data are necessary

A publicly reachable web server cannot be operated and protected meaningfully without processing the requests made to it. IP/request/error information can be necessary to detect malicious activity, troubleshoot failures and maintain service integrity.

Hostinger generates access logs as part of the hosting infrastructure. ConflictLab does not add a custom user fingerprint or marketing tracker to reproduce the same function.

### Less intrusive alternatives considered

```text
Disable all server/security logs entirely
-> would materially reduce security/troubleshooting ability.

Add Google Analytics / marketing analytics
-> unnecessary and more intrusive for the stated purpose; not used.

Copy Hostinger access logs into research DB
-> unnecessary; prohibited by architecture.

Store full User-Agent/IP in ConflictLab timing tables
-> unnecessary; not implemented.
```

### Minimisation controls

- research DB does not intentionally store IP address;
- research DB stores only coarse device category rather than full fingerprint;
- access/security logs remain provider/technical data, separate from research analysis;
- no advertising identifiers;
- no persistent cross-site participant tracking;
- no use of access logs to derive CS/CR or other participant interpretations.

### Conclusion

```text
NECESSITY TEST = PASS FOR CURRENT NARROW SCOPE
```

If technical logs are later repurposed for product analytics or participant research, this conclusion must be reopened.

## 5. Balancing test

### Data-subject interests / potential impact

Relevant risks include:

- an IP address may relate to an identifiable person/connection;
- request URLs/timestamps can reveal use of the service;
- User-Agent/device information increases technical observability;
- security logs can be sensitive if access is excessive or retention is unjustified;
- combining logs with research records would materially increase impact.

### Reasonable expectations

A visitor to a public web service can reasonably expect proportionate technical logging for security, availability and error diagnosis, particularly when this use is transparently disclosed.

They should not reasonably be expected to infer that the same technical logs are used for psychological research or advertising. ConflictLab therefore explicitly forbids that repurposing under this LIA.

### Safeguards reducing impact

```text
purpose restriction: security / operation only
data separation: access logs != timing research DB
no advertising use
no psychological use
no custom fingerprinting
HTTPS
Hostinger account/admin access controls
research DB minimisation
privacy notice disclosure
processor DPA/security obligations
```

Hostinger documentation reviewed for the web analytics interface exposes up to a 7-day filter for hPanel website request analytics, but the exact underlying provider log lifecycle is not inferred beyond what Hostinger documents. ConflictLab does not copy those logs into a longer-lived research store.

### Children

The intended external calibration research is adult-only. The general OMESG360 website itself is public, so technical security processing must remain proportionate even if a minor accesses the website incidentally.

### Conclusion

```text
BALANCING TEST = PASS FOR CURRENT NARROW SECURITY/OPERATIONAL SCOPE
```

The conclusion depends on keeping the safeguards and separation above.

## 6. Right to object / transparency

The public privacy information should state:

- that technical Hostinger access/security logs may contain IP/request/device-derived information;
- that the purpose is service operation/security/diagnosis;
- that these logs are separate from ConflictLab research data;
- privacy contact: `info@omesg360.eu`;
- applicable data-subject rights, including objection where Article 6(1)(f) applies.

An objection must be assessed under the GDPR rather than automatically rejected merely because the processing is described as security-related.

## 7. Processor boundary

Hostinger DPA reviewed 2026-08-15 describes the shared responsibility model: Hostinger maintains infrastructure security controls while the customer remains responsible for configuring the service and using available access/security/deletion controls appropriately.

This LIA does not replace the Hostinger DPA or processor review.

## 8. Decision

```text
LEGAL BASIS CANDIDATE:
GDPR Art. 6(1)(f) legitimate interests

AUTHORIZED SCOPE:
strictly necessary and proportionate website/server security,
integrity, abuse prevention and technical troubleshooting

NOT AUTHORIZED BY THIS LIA:
optional timing research
Gate D/E research
marketing analytics
advertising
participant profiling
psychological interpretation
joining security logs with the research DB
```

## 9. Reopen triggers

Reassess this LIA before any of the following:

- installing a new analytics/tracking product;
- retaining IP/User-Agent data inside ConflictLab research tables;
- joining provider logs with participant/session records;
- using request logs for behavioural/product research rather than security;
- materially extending log retention under controller control;
- introducing account-based persistent identities;
- changing the security purpose or recipient set.

## 10. Sources reviewed

```text
GDPR Article 6(1)(f) and Recital 49
EDPB Guidelines 1/2024 / EDPB legitimate-interest three-condition summary
Hostinger hPanel Analytics / Access Logs documentation
Hostinger Data Processing Addendum, reviewed 2026-08-15
```

This internal assessment is a documented controller decision, not a substitute for qualified legal advice if the processing scope/risk materially expands.
