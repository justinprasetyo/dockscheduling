# dockscheduling
Dock Scheduling System
**Please allow up to 60 seconds for the live demo to wake up on the first load.**
live url: https://dockscheduler.onrender.com

PROBLEM:
A WHOI marine research facility needs to manage berths of varying lengths. Vessels reserve a berth for specific ranges of days. The waterfront also hosts non-vessel events such as community sail days that also occupy a berth.

A sample schedule is attached to this email, containing 23 years of bookings. Some issues include the need to manually check for double-bookings by looking at a grid and verifying that a vessel actually fits the berth it has been assigned to.

Build a system to manage these reservations.

DOCKS LIST:
dock number 1: North Pier West - 410'
dock number 2: North Pier Face - 75'
dock number 3: North Pier East - 240'
dock number 4: Inner Channel - 55'
dock number 5: South Float West - 90'
dock number 6: South Float East - 90'

FEATURES:

error checks:
_vessel dimensions are capped (max lengths are at the end of every dock's name in feet), *max widths of docks are assumed.

_vessel dimensions can't be less than 0. this case will throw an error on the screen.

_if event doesn't include a vessel, users are expected to write 0 for both vessel dimensions and state the lack of a vessel in the reason input.

_dates cannot collide with other reservations'. *end date is inclusive, a boat is expected to leave the night of the end date (not the morning); (if the starting and end date are the same, a boat is expected to come the morning of the start date and take up that whole day).

_starting dates cannot be more than the end date. this case will throw an error on the screen.

_