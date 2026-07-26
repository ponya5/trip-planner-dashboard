---
name: trip-dashboard
description: Build a single self-contained, interactive HTML trip-planning dashboard for any multi-day trip — road trip, adventure/off-road itinerary, train/city-hopping tour, or family vacation. Includes a live-routed map (real roads via OpenStreetMap/OSRM, not straight lines), day-by-day colour-coded routes and POIs, a drive-the-trip playback animation with adjustable speed, transportation cost comparisons (rental vehicles, trains, flights), hotels with price bands and booking links, budget, packing list, pre-trip checklist, and safety/weather fallbacks. Use whenever the user wants to plan a multi-day trip and would benefit from a visual plan instead of a plain list — even if they just say "help me plan a trip to X" or "we're driving around Y for a week," without asking for a "dashboard" or "map." Also use to update a dashboard this skill previously built (change a route, fix distances, re-cost transport).
---

# Trip Dashboard

Turns a destination + dates + travel style into a single HTML file the traveler can open in any browser: a live-routed map on one tab, and a full written trip plan on the other. No server, no API key, no build step — everything runs client-side off free services (OpenStreetMap tiles, the public OSRM routing API, Google Maps deep-links).

## What this builds

Every dashboard this skill produces includes:

- **Live-routed map** — Leaflet + OpenStreetMap tiles, with each day's route drawn twice: a dotted "planned" straight line (the intent) and a thick "live" line calculated by the OSRM routing engine following actual roads, with measured km and drive time. Both are explained to the traveler side by side so they know which number to trust.
- **Drive-the-trip playback** — an animated marker drives each day's route in sequence on request, with a 0.25×–4× speed control, plus an ambient flowing-dash animation on every route that can be paused/resumed.
- **Day-by-day itinerary** — colour-coded per day, with timed POI stops, tips, and tags for overnight stays, weather-sensitive legs, light off-road sections, and shopping stops. Each day links out to Google Maps with turn-by-turn navigation.
- **Transportation section** — whatever fits the trip: rental vehicle comparisons (car/SUV/4x4) with daily rates, train fares and routes, or flight segments, plus a running fuel/ticket cost estimate.
- **Hotels & lodging** — price bands and booking links per stop, sized to the group.
- **Budget, food, packing, and a pre-trip checklist** — practical sections a traveler actually uses in the weeks before departure.
- **Safety & fallbacks** — what to do if a pass closes, weather turns, or a road is impassable, with concrete alternates rather than "be careful."
- **A day-isolation legend and draggable map/sidebar divider** so the dashboard stays usable on any screen size.

This skill was distilled from building a real 6-day Georgia (the country) 4x4 road trip dashboard across many rounds of user feedback. The engine — map, live routing, playback, layout — is solved and bundled in `assets/dashboard_template.html`. **Don't rewrite that engine from scratch.** Your job each time is to research the specific trip and fill in the content; the template handles rendering, animation, and the two hardest bugs already (see "Known traps" below).

## See it working: the demo trip

`examples/demo-trip.html` is a complete, ready-to-open dashboard for a short 4-day San Francisco → Big Sur loop — open it in a browser to see every feature live before building a real one: the live-vs-planned routing, the drive/playback controls, the day legend, hotels, budget, and the optional-extras toggle. It also demonstrates something worth copying in every dashboard you build: Day 2 (Monterey → Big Sur → Monterey) is a genuine out-and-back, because Big Sur has no through road — the demo says so plainly instead of pretending it's a loop. That honesty is part of what this skill is for, not a flaw to paper over.

Use the demo as a reference for structure and tone, not as a starting point to copy-paste from — always build a new trip from `assets/dashboard_template.html`.

## Before you start: gather the trip shape

You need answers to these before you can write good content. If the user's request already answers most of them, don't re-ask — just confirm the gaps:

1. **Destination and route shape.** One region driven in a loop? A point-to-point? Multiple cities linked by train/flight? A loop matters a lot: users planning a loop almost always want to avoid driving the same road twice — treat that as a real constraint, not a nice-to-have, and check it against actual road geography (see below).
2. **Dates and trip length.** Total days, and roughly how many are driving days vs. rest/city days.
3. **Group size and transport.** How many people, how many vehicles, rental or self-driven, any 4x4/off-road requirement.
4. **Flights or fixed arrival/departure**, if any — times matter for realistic Day 1/last-day planning.
5. **Interests and pace.** Adventure/off-road vs. paved and relaxed, food, wine, hiking, shopping, family-friendly, budget level. This shapes which POIs you pick and how much buffer time each day gets.

Ask only what's missing, in one batch, not one question at a time.

## Research before writing content

This is the part that actually takes judgment. Do not invent coordinates, prices, road conditions, or distances — search for them. Specifically:

- **Verify roads exist and are drivable** before building a route around them, especially for "shortcuts" or lesser-known mountain/rural roads. A road that looks plausible on a mental map can be seasonal, unpaved-only, or simply not connect the way you'd guess. Search for recent trip reports or official sources, not just intuition.
- **Get real coordinates** for POIs (search "<place> coordinates" or pull from a mapping source) — don't guess lat/lon from general geography, it's an easy way to place a marker in the wrong town.
- **Get real distances/times** for the legs you're planning, particularly for a claimed "shortcut" or "direct route" — if the user gives you a screenshot of a mapping app's route (as sometimes happens), match your plan to what's actually shown, not to your own estimate.
- **Price bands**, not point prices, for rentals/hotels/food — search current listings and give ranges, and say so ("check current rates").

If the user pushes back that a route is too long, doubles back, or doesn't match a map they're looking at, that is a strong signal your distance/road assumption was wrong — re-verify rather than defending the original number.

## Build the dashboard

1. Copy `assets/dashboard_template.html` to the output location — don't start from a blank file.
2. Fill in the `const TRIP = {...}` object near the top of the `<script>` block. This is the single source of content: title, subtitle, the `days[]` array (each with POIs, times, tips), `hotels[]`, `budget`, `food`, `packing`, `checklist`, `safety`, and `alternates[]` (optional add-ons/swaps, e.g. weather fallback plans). The template's rendering code, map logic, and CSS already reference these fields — see the comments inside the template for the exact shape each field needs.
3. Update the static prose sections in the "Full Trip Plan" tab (overview text, risk call-outs, why-this-shape explanation) to match the actual trip — these are hand-written narrative, not auto-generated from `TRIP`, because good trip narrative explains *why* a route works, which a template can't infer.
4. Every time you change a day's distance or POIs, re-check every place that number appears: the day's own row, the route table, the grand total, the fuel/budget math, and any narrative sentence that quotes it. A stale number in one section after fixing another is the single most common mistake in this kind of dashboard — grep for the old figure before declaring a change done.
5. Verify the JS is syntactically valid before calling it finished: run `scripts/verify_js.py <path-to-html>`. This extracts the `<script>` block and runs `node --check` on it — it catches the kind of typo that would otherwise only surface as a silent blank map in the browser.
6. Save the finished file to the user's output folder and present it. Don't just describe it in chat — the deliverable is the file itself.

## Known traps (already solved in the template — don't reintroduce them)

- **Live routing can silently invent a huge detour.** The public OSRM router follows OpenStreetMap's road graph, which doesn't always have new, resurfaced, or obscure roads tagged as drivable. If a real road is missing from that data, OSRM doesn't error — it quietly routes the long way around (sometimes literally backtracking through where you came from), and a naive dashboard will show that wrong loop as "the real route." The template checks each routed leg's distance against the straight-line distance between its endpoints and falls back to a straight planned line for that day if a leg is more than 3x the straight-line distance — see `haversineM()` and the leg-check inside `routeDay()`. Keep this check; it's what prevents a bogus multi-hour detour from ever being presented as fact.
- **Layout/scroll bugs from mixing scroll containers.** The template uses two page-level modes — `body.map-mode` (locked height, JS measures the viewport and sizes the map pane exactly) and `body.details-mode` (native page scroll) — because nested `overflow-y:auto` containers are unreliable across embedding contexts. Don't replace this with a single flexbox-scroll layout; it's the thing that broke repeatedly before this pattern was adopted.
- **A "loop" isn't automatically a loop.** Don't assume a route avoids repeating roads just because the day labels look different — actually trace the geography. If two days share a road (e.g., the only road in and out of a dead-end valley), say so explicitly rather than claiming a false "no repeats."

## Privacy

Never write a specific person's flight numbers, names, or other personal booking details into the skill files themselves — those belong only in the generated dashboard delivered to that user for that trip. The skill (this file and its template) must stay generic so it works identically for anyone's trip. When building a dashboard, put the user's specifics only in the output HTML file, never back into `assets/dashboard_template.html`.

## Common revisions

Users iterate on these dashboards a lot after the first draft — treat that as normal, not as a sign something went wrong the first time:
- "Change the route for day N" → re-verify the new leg's real road/distance before editing, then propagate the number everywhere it's quoted (step 4 above).
- "Add tooltips / I can't read the truncated text" → add a `title` attribute with the full text next to any place you truncate a label with CSS ellipsis or `.slice()`.
- "This shouldn't drive the same road twice" → treat as a hard constraint on route planning, not a copy-editing note; re-derive the physical route.
- "Add playback speed / slow down the animation" → the template's drive-animation already supports a speed multiplier control; wire new UI to the existing `driveSpeed` variable rather than duplicating the animation loop.

## For humans: installing and using this skill

This section is for the person setting the skill up, not for Claude while it's building a dashboard.

**Folder layout you should have:**
```
trip-dashboard/
├── SKILL.md
├── assets/dashboard_template.html   (the reusable engine)
├── examples/demo-trip.html          (open this in a browser to see it work)
├── scripts/verify_js.py             (JS syntax check)
└── evals/evals.json                 (test prompts used while developing this skill)
```

**To use it yourself:** just ask Claude to plan a multi-day trip — "plan a 7-day road trip through Scotland for 4 of us" is enough. Claude will read this SKILL.md automatically once it's installed in one of the locations below and recognizes the request as a trip-planning task.

**Where to install it, depending on where you use Claude:**
- **Claude Code:** drop the whole `trip-dashboard/` folder into `~/.claude/skills/` (personal, available in every project) or `<project>/.claude/skills/` (shared with anyone who has that repo).
- **claude.ai:** zip the `trip-dashboard/` folder and upload it under Settings → Features → Skills (requires a Pro/Max/Team/Enterprise plan with code execution enabled). This is per-person — each user uploads their own copy.
- **Claude API / Cowork:** upload via the Skills API (`/v1/skills`) if you're building on the API directly; it becomes available workspace-wide.

There's no single step that makes a custom skill available to "everyone on Claude" at once — see the sharing note below.
