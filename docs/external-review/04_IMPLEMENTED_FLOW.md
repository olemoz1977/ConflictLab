# 04 — Implemented Flow

This describes only the flow that actually runs in the current Pair P0 code.

```
pair selection
  → cue or own words
  → session summary
  → literal display of chosen words
  → user names or does not name a connection
  → feedback
  → history
  → optional radar
  → export/import
  → local data reset
```

## Step by step

### 1. Pair selection
- **Stored:** pair ID, top/bottom image IDs, which image was selected, position, choice latency (ms)
- **Shown:** two images, side by side or stacked; person taps one
- **Not interpreted:** the system does not infer why an image was chosen

### 2. Cue or own words
- **Stored:** the cue ID and text if a pre-written phrase was chosen; the person's own text if "Another thought" was chosen; a "hard to say" marker if that was chosen; an optional short (≤5 word) individual reflection tied to that specific choice
- **Shown:** three pre-written phrases plus "Another thought" and "Hard to say" options
- **Not interpreted:** no theme, category, or trait is assigned to any cue at this stage

### 3. Session summary (session reflection)
- **Stored:** one free-text observation about the session as a whole, or an explicit "not yet named" marker
- **Shown:** all three chosen images with their selected wording, then one open question
- **Not interpreted:** the system does not judge whether the person's observation is correct or complete

### 4. Literal display of chosen words (Stage I)
- **Stored:** nothing new — this step displays existing data
- **Shown:** "What you chose in this session," listing the exact wording selected for each of the three pairs, in order, using this source priority: the person's own written words first, the chosen cue text second, or "This choice was left unstated" if neither exists
- **Not interpreted:** no grouping, theme, or category is applied to the three displayed choices

> **"Your observation" is the person's own text, not a ConflictLab conclusion.** This label appears only above verbatim user-authored text, never above system-generated text.

### 5. User names or does not name a connection
- **Stored:** `session_connection_reflection` — one of three explicitly distinct response types: `text` (the person's own words), `not_seen_yet`, or `prefer_not_to_state`
- **Shown:** the question "Do you notice anything that may connect these choices?" with three separate answer options and a single shared "Continue"/"Finish session" action (no separate save button)
- **Not interpreted:** "not_seen_yet" and "prefer_not_to_state" are stored and displayed as distinct states; the system never collapses them into a single "no response" category, and neither is treated as a deficit

### 6. Feedback
- **Stored:** four yes/no questions about the experience plus an optional free-text reason
- **Shown:** standard feedback screen
- **Not interpreted:** answers are stored as given

### 7. History
- **Stored:** nothing new; reads from `completed_sessions`
- **Shown:** a list of completed sessions with date, choice count, and (per the Stage I precedence fix) either the new `session_connection_reflection` text or, only if that field does not exist, the older `session_reflection` fallback text — never both at once
- **Not interpreted:** each session's history entry is a direct record, not a summary or trend statement

### 8. Optional radar
- **Stored:** nothing new; computed from `completed_sessions` that meet eligibility criteria (status completed, a valid session vector, at least 2 valid vector responses, a finite confidence value, matching vector-model version, and axis values within [-1, 1])
- **Shown:** appears only behind a "View your current trace" link, collapsed by default; a bipolar six-direction chart, exact numeric values, and an explicit note that this is not a personality assessment
- **Not interpreted:** ineligible sessions remain visible in history but are excluded from this calculation without being deleted or silently migrated

### 9. Export/import
- **Stored/Read:** a local JSON file containing only completed sessions, schema-versioned; import merges by `session_id`, with local records never overwritten by imported duplicates
- **Shown:** an import summary (imported / already-on-device / invalid counts)
- **Not interpreted:** no network request is made at any point in export or import

### 10. Local data reset
- **Stored/Removed:** deletes only `localStorage` keys beginning with the Pair P0 namespace prefix (`cl_pair_p0_`); requires an explicit checkbox before the destructive action is enabled
- **Shown:** a confirmation modal listing exactly what will be removed, with a note about the active (unfinished) session if one exists
- **Not interpreted:** this step performs no analysis; it is a housekeeping function

## Backward compatibility with older (Stage H) sessions

Sessions completed before Stage I was implemented do not have a `session_connection_reflection` field. For these sessions, the history display falls back to the older `session_reflection` field and its associated neutral fallback text. No data is invented or migrated for older sessions; the absence of the newer field is handled as a normal, expected case, not an error.
