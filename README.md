# Trip Planner Dashboard

<img src="assets/tripIntro.jpeg" alt="Trip Planner Dashboard" width="40%" />

An AI **skill** that turns “plan me a trip” into one HTML file you can open in any browser. You get a live map on one tab and a full written plan on the other (days, hotels, budget, packing, safety). Works with Claude, Cursor, and other tools that support skills. No server. No API key. No build step. It uses free map and routing services in the browser.

### **Personal note. Why I created this skill**

I built this after planning a real 6-day jeep trip in Georgia (the country). The first versions had wrong turns, a fake 300 km detour from bad map data, layout bugs, and no easy way to “drive” the route on the map. After fixing those pieces over many rounds, I packed the working parts into this skill so the next “plan my trip” request starts from something that already works, not from a blank file.

### **Screenshots**

![Map and Routes tab](assets/trip1.png)

*Demo trip. Map and Routes tab with live routes and playback controls.*

![Map and Routes day itinerary](assets/trip4.png)

*Map and Routes tab. Day list with stops, Google Maps link, and Drive this day.*

![Full Trip Plan overview](assets/trip2.png)

*Full Trip Plan tab. Trip overview and road notes.*

![Full Trip Plan itinerary](assets/trip3.png)

*Full Trip Plan tab. Day-by-day itinerary and vehicle options.*

### **Features**

- **Live-routed map.** Each day shows a dotted planned line and a thick live line on real roads, with distance and drive time.
- **Detour-safe routing.** If the live route looks impossible, the dashboard falls back to the planned line instead of showing a bad detour.
- **Drive-the-trip playback.** Watch a marker drive the route. Change speed. Pause or resume the flowing route animation.
- **Day-by-day itinerary.** Colour by day, with stops, tips, and a Google Maps link for each day.
- **Transportation costs.** Cars, trains, or flights, with rough price ranges.
- **Hotels and lodging.** Price bands and booking links for your group size.
- **Budget, food, packing, and a pre-trip checklist.**
- **Safety and fallbacks.** What to do if a road closes or weather turns bad.
- **Works on phone and desktop.** Day filters, a draggable split view, and helpful tooltips.

### **See it working**

Open [`examples/demo-trip.html`](examples/demo-trip.html) in your browser. No install needed. It is a short 4-day San Francisco to Big Sur demo. Day 2 goes Monterey to Big Sur and back, because there is no through road south. The plan says that clearly.

### **Where it works**

The same folder works with **Claude** and with **Cursor**. Other AI coding tools that support skills can use it too. Put the folder in that tool’s skills place, then ask it to plan a trip.

### **How to use it with Claude**

#### **On the Claude website (claude.ai)**

**How to get the zip file**

1. Open this project’s page on GitHub.
2. Click the green **Code** button near the top right.
3. Click **Download ZIP**.
4. Wait for the download to finish. You will get a file like `trip-dashboard-skill-main.zip` in your Downloads folder.
5. Keep that zip as is. You do not need to unzip it for the website upload.

**How to add the skill on claude.ai**

1. Open [claude.ai](https://claude.ai) and sign in.
2. Go to **Settings**, then **Features**, then **Skills**.
3. Upload the zip you downloaded. You need a plan that allows Skills (Pro, Max, Team, or Enterprise, with code execution on).
4. Start a new chat.
5. Type what you want, for example  
   `Plan a 7-day road trip through Scotland for 4 of us, renting one car.`
6. Answer any follow-up questions (dates, budget, and so on).
7. When Claude finishes, open or download the HTML file it made. Double-click it to open in your browser.

#### **In Claude Code (on your computer)**

1. Get the project folder. Either download the zip (steps above) and unzip it, or copy the folder if you already have it.
2. Put that folder here so Claude can find it  
   - For every project on your computer  
     `~/.claude/skills/trip-dashboard/`  
   - Or only for one project  
     `your-project-folder/.claude/skills/trip-dashboard/`
3. Close Claude Code and open it again (or start a new chat).
4. Type a trip request in normal words, like the example above.
5. Open the HTML file Claude saves. Use your browser.

#### **With the Claude API or Cowork**

1. Upload this skill with the Skills API.
2. Ask for a trip plan in normal words, same as above.

### **How to use it with Cursor**

1. Get the project folder. Download the zip from GitHub (green **Code** button, then **Download ZIP**), unzip it, or copy the folder if you already have it.
2. Put that folder here so Cursor can find it  
   - For every project on your computer  
     `~/.cursor/skills/trip-dashboard/`  
   - Or only for one project  
     `your-project-folder/.cursor/skills/trip-dashboard/`  
   Tip. If you already put it under `.claude/skills/` for Claude, Cursor can often use that copy too. You do not need two copies.
3. Restart Cursor, or open a new **Agent** chat.
4. In Agent, type what you want in normal words. Examples  
   - `Plan a 7-day road trip through Scotland for 4 of us, renting one car.`  
   - `Build me a family trip dashboard. Oregon coast, 5 days, driving from Portland, kid-friendly.`  
   You can also type `/trip-dashboard` and then describe the trip.
5. Answer any questions the agent asks.
6. When it is done, open the HTML file it created in your browser.

### **Things you can say (Claude or Cursor)**

- Plan a 7-day road trip through Scotland for 4 of us, renting one car.
- We are doing a 10-day Italy trip by train. Rome, Florence, Cinque Terre, Venice. Food and wine over museums.
- Build me a family trip dashboard. Oregon coast, 5 days, driving from Portland, kid-friendly.

The AI may ask for dates, group size, transport, or budget if you left those out. Then it builds one HTML file you can open offline in a browser (the map still needs internet for tiles and live routing).

### **What is in this folder**

```
trip-dashboard-skill/
├── README.md                        (this file)
├── SKILL.md                         (instructions the AI reads)
├── assets/
│   ├── dashboard_template.html      (map and plan engine)
│   ├── tripIntro.jpeg               (README intro image)
│   ├── trip1.png                    (screenshot, Map and Routes)
│   ├── trip2.png                    (screenshot, Trip overview)
│   ├── trip3.png                    (screenshot, Day-by-day itinerary)
│   └── trip4.png                    (screenshot, Day sidebar on map)
├── examples/
│   └── demo-trip.html               (working demo you can open now)
├── scripts/
│   └── verify_js.py                 (checks the dashboard JavaScript)
└── evals/
    └── evals.json                   (test prompts from development)
```

### **License**

MIT. Use it, fork it, adapt it for your own trips.
