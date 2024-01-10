from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

utc_now = datetime.now(timezone.utc)
print(utc_now)

local_now = utc_now.astimezone()
print(local_now)

new_york_tz = zoneinfo.ZoneInfo('America/New_York')
ny_now = utc_now.astimezone(tz=new_york_tz)
print(ny_now)


paris_tz = zoneinfo.ZoneInfo('Europe/Paris')

france = utc_now.astimezone(paris_tz)
print(france)

print()

print('Available timezone keys')
print("-----------------------")

for zone_key in sorted(zoneinfo.available_timezones()):
    print(zone_key)

