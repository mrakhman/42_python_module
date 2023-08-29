from datetime import datetime
now = datetime.now()
timestamp = datetime.timestamp(now)

print(f'Seconds since January 1, 1970: {timestamp:,.4f} \
or {timestamp:0.2e} in scientific notation')

formatted_date = now.strftime("%b %d %Y")
print(formatted_date)
