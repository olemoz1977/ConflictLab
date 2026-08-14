# Public entrypoint switch template

This is a **non-executable repository template** for the future public switch. It must not be copied to Hostinger before explicit PUBLIC authorization.

Target behavior:

```text
/wave1/
  -> /conflictlab/releases/<OWNER_APPROVED_RELEASE_ID>/
```

The live switch artifact should be intentionally tiny and static. It should contain only:

1. a redirect target pointing at the immutable approved release path;
2. a simple manual fallback link to the same target;
3. no participant logic, scoring, API writes or methodology configuration.

Before installing the switch artifact:

```text
1. Save the exact current /wave1/index.html as the rollback artifact.
2. Verify the approved release path directly on mobile.
3. Verify its release manifest and source commit SHA.
4. Confirm owner approval.
5. Obtain a separate explicit PUBLIC switch authorization.
6. Replace only /wave1/index.html.
7. Smoke-test the stable published /wave1/ URL.
```

Rollback:

```text
restore the saved previous /wave1/index.html
```

Do not delete the failed/new release during rollback. Keep it for diagnosis and provenance.
