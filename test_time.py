from datetime import datetime, timezone
import zoneinfo

# utc_now = datetime.now(timezone.utc)
#
# time_london = zoneinfo.ZoneInfo('Europe/London')
# london_time = utc_now.astimezone(time_london).replace(microsecond=00)
# print(f"The time in london now is     {london_time}")
#
#
# paris_tz = zoneinfo.ZoneInfo('Europe/Paris')
# france = utc_now.astimezone(paris_tz).replace(microsecond=0)
# print(f"The time in Paris now is      {france}")
#
#
# time_honkong = zoneinfo.ZoneInfo('Asia/Hong_Kong')
# hongkong_time = utc_now.astimezone(time_honkong).replace(microsecond=0)
# print(f"The time in Hong Kong now is  {hongkong_time}")
#
#
# time_nairobi = zoneinfo.ZoneInfo('Africa/Nairobi')
# nairobi_time = utc_now.astimezone(time_nairobi).replace(microsecond=0)
# print(f"The time in Nairobi now is    {nairobi_time}")
#
zones = (
    'Europe/London',
    'Europe/Paris',
    'Asia/Hong_Kong',
    'Africa/Nairobi')
utc_now = datetime.now(timezone.utc)
utc_now = utc_now.replace(microsecond=0)
for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    required_time= utc_now.astimezone(tz)
    city = zone.split('/')[-1]
    print(f'The time in {city} is {required_time} {required_time.tzname()}')
    # print(f'The time in {city} is {required_time.strftime(" %m/%d/%Y %H:%M:%S %z %Z")}')
