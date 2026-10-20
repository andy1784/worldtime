# Glossary

*This file is maintained by `/domain-modeling` (reached via `/grill-with-docs` and `/improve-codebase-architecture`). Terms are added lazily when they are actually resolved during grilling sessions.*

---

# Meeting Planner v2

## Language

**Meeting Plan**:
A shareable, signed URL containing a team's cities, recurrence rule, rotation policy, preferred windows, meeting title/duration, and reminder emails — fully self-contained, verifiable without backend.
_Avoid_: Meeting config, scheduling link, team schedule

**Rotation Policy**:
The algorithm that selects the meeting time for each occurrence of a recurring meeting; v2 uses "intersection rotation": rotate through UTC slots that fall within every member's preferred window.
_Avoid_: Fairness algorithm, rotation logic, scheduling rotation

**Preferred Window**:
A member's self-declared acceptable local hours (e.g., 07:00–22:00); meetings outside this window count as "burden" for fairness scoring.
_Avoid_: Availability, working hours, time preference

**Burden Score**:
A per-member counter of how many meeting occurrences have fallen outside their preferred window; used to bias rotation toward fairness.
_Avoid_: Penalty score, unfairness metric, off-hours count

**Signed Plan URL**:
A base64url-encoded JSON payload + HMAC signature (HS256, secret in env) that encodes a complete Meeting Plan; tamper-evident, no database lookup needed.
_Avoid_: Encrypted URL, token, share link

**Heatmap Overlay**:
A visual layer on the multi-week grid where cell color intensity = count of members in business hours at that UTC hour; hover reveals names.
_Avoid_: Density map, overlap visualization, grid coloring

**DST Transition Week**:
A calendar week where at least one selected city's time zone changes offset; highlighted in the grid with a stripe and tooltip.
_Avoid_: DST change week, timezone transition week

**VALARM**:
An iCalendar component (`BEGIN:VALARM`) embedded in generated `.ics` files that triggers a client-side notification (e.g., 15 min before) — works in Google/Outlook/Apple Calendar without any backend.
_Avoid_: Calendar alarm, reminder trigger, notification component