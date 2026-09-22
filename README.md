# Dock Scheduling System
**Please allow up to 60 seconds for the live demo to wake up on the first load.**
live url: https://dockscheduler.onrender.com

## DOCKS LIST:
dock number 1: North Pier West - 410'
dock number 2: North Pier Face - 75'
dock number 3: North Pier East - 240'
dock number 4: Inner Channel - 55'
dock number 5: South Float West - 90'
dock number 6: South Float East - 90'

## Running locally
git clone https://github.com/justinprasetyo/dockscheduling.git
pip install -r requirements.txt
python3 app.py

## Assumptions
- End date is inclusive; a boat is expected to leave the night of the end
  date, not the morning
- Dock widths aren't in the sample data, so I estimated them (list them)
- Non-vessel events are entered with vessel dimensions of 0

## Design
- One SQL query checks for date overlap on a dock: two ranges overlap when
  each starts on or before the other ends
- Booking is a two-step confirm; the server rechecks at confirm time,
  not just on the initial check when you press 'Enter'
- Substring filter for dock/start/end date/reason using SQL LIKE %%

## Short term limitations
- Free hosting sleeps after inactivity; first load can take ~60s
- The database resets on a cold restart (I seeded it to have some example reservations on startup)

## Future ideas
- Make an import script to import the 23 year sample schedule and add an audit view for existing
  conflicts and oversized vessels for even more security against mistakes
- Ability to sort (instead of only filter out) reservations by clicking column headers