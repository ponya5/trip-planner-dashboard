# trip-dashboard

A Claude Agent Skill that turns "plan me a trip" into a single, self-contained, interactive HTML dashboard — a live-routed map on one tab, and a full written trip plan (itinerary, hotels, budget, packing, safety) on the other. No server, no API key, no build step. Everything runs client-side off free services: OpenStreetMap tiles, the public OSRM routing API, and Google Maps deep-links.

![Trip dashboard screenshot](screenshot.png)
*The demo trip (`examples/demo-trip.html`) open in Chrome — Map & Routes tab.*

## Features

- **Live-routed map.** Each day's route is drawn twice: a dotted "planned" straight line (the intent — which stops, in what order) and a thick "live" line calculated on load by the OSRM routing engine following actual roads, with measured km and drive time. The dashboard explains the difference to the traveler so they know which number to trust.
- **Detour-safe routing.** Public routing data doesn't always have brand-new or resurfaced roads tagged as drivable — when that happens, naive routing tools silently invent a huge, wrong detour instead of erroring. This skill checks every routed leg against the straight-line distance between its endpoints and falls back to the planned line if a leg looks physically impossible, so a bogus multi-hour detour never gets presented as fact.
- **Drive-the-trip playback.** An animated car marker drives each day's route in sequence on request, with a 0.25×–4× speed control, plus an ambient flowing-dash animation on every route that can be paused and resumed.
- **Day-by-day itinerary.** Colour-coded per day, with timed POI stops, tips, and tags for overnight stays, weather-sensitive legs, light off-road sections, and shopping stops. Every day links out to Google Maps with turn-by-turn navigation.
- **Transportation costs.** Whatever fits the trip — rental vehicle comparisons (car/SUV/4x4) with daily rates, train fares and routes, or flight segments — plus a running fuel/ticket cost estimate.
- **Hotels & lodging** with price bands and booking links, sized to the group.
- **Budget, food, packing, and a pre-trip checklist** — the practical sections a traveler actually uses in the weeks before departure.
- **Safety & fallbacks** — concrete alternates if a pass closes or weather turns, not generic "be careful" advice.
- **Usable on any screen.** A day-isolation legend, a draggable divider between the map and the sidebar, and tooltips on anything that gets visually truncated.

## See it working

Open [`examples/demo-trip.html`](examples/demo-trip.html) directly in a browser — no setup needed. It's a short 4-day San Francisco → Big Sur loop, chosen because it exercises every feature above, including one thing worth noting: Day 2 (Monterey → Big Sur → Monterey) is a genuine out-and-back, because Big Sur has no through road south. The dashboard says so plainly instead of pretending it's a loop — that honesty about real road geography is a core design goal of this skill, not an afterthought.

## How to install

**Claude Code:** drop this whole folder into `~/.claude/skills/` (personal, available in every project) or `<project>/.claude/skills/` (shared with anyone who has that repo — e.g. by cloning this repo into that path).

**claude.ai:** download this repo as a zip, then upload it under Settings → Features → Skills (requires a Pro/Max/Team/Enterprise plan with code execution enabled). This is per-person — each user uploads their own copy; skills don't sync across accounts automatically.

**Claude API / Cowork:** upload via the Skills API (`/v1/skills`) if you're building on the API directly — it becomes available workspace-wide.

There's no single official "app store" step that makes a custom skill available to everyone at once. See [Anthropic's Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) for the full picture of where skills are supported and how sharing scope differs per surface.

## How to use it

Once installed, just ask Claude to plan a trip in plain language — no special syntax needed:

- "Plan a 7-day road trip through Scotland for 4 of us, renting one car."
- "We're doing a 10-day Italy trip by train — Rome, Florence, Cinque Terre, Venice. Food and wine over museums."
- "Build me a family trip dashboard — Oregon coast, 5 days, driving from Portland, kid-friendly."

Claude will ask for anything essential that's missing (dates, group size, transport, budget level), research real roads/coordinates/prices rather than guessing, and then build and save the dashboard file.

## Repository layout

```
trip-dashboard-skill/
├── README.md                        (this file)
├── SKILL.md                         (the skill definition Claude reads)
├── assets/
│   └── dashboard_template.html      (the reusable engine — map, routing, playback, layout)
├── examples/
│   └── demo-trip.html               (a working demo you can open right now)
├── scripts/
│   └── verify_js.py                 (checks the generated dashboard's JS for syntax errors)
└── evals/
    └── evals.json                   (test prompts used while developing this skill)
```

## Why this skill exists

This was distilled from building a real 6-day, 3-jeep road trip dashboard for the country of Georgia across many rounds of back-and-forth feedback — fixing route directions that doubled back on themselves, catching a routing-data bug that silently invented a 300km detour, layout/scroll bugs, and adding a playback feature. Rather than solve each of those problems again for the next trip, the reusable parts got packaged here so any future "plan me a trip" request starts from a working, battle-tested engine instead of a blank file.

## License

MIT — use it, fork it, adapt it for your own trips.
