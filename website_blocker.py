# Set to always run as admin.

import time
from datetime import datetime as dt

# For Mac/Linux use '/etc/hosts' instead.
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

# List of websites you want blocked.
websites = ['www.facebook.com', 'www.twitter.com']

# Where to redirect users trying to visit blocked websites.
redirect = '127.0.0.1'

# Hours the website ban is active(24-hour format, pass the hour as the last value).
start = dt(dt.now().year, dt.now().month, dt.now().day, 9)
finish = dt(dt.now().year, dt.now().month, dt.now().day, 17)

# Keep the process always running in the background.
while True:
	if start < dt.now() < finish:
		with open(hosts_path, 'r+') as f:
			content = f.read()
			for website in websites:
				if website in content:
					pass
				else:
					f.write(redirect + ' ' + website + '\n')
	else:
		# Make the ban inactive during off hours.
		with open(hosts_path, 'r+') as f:
			content = f.readlines()
			# f.write() pointer for writing at the top/start of the file
			f.seek(0)
			for line in content:
				# Remove blocked websites from hosts file during off-hours
				if not any(website in line for website in websites):
					f.write(line)
				# Keep what was just written to the file(in the above two lines)
				# and delete the old content of the hosts file.
				f.truncate()
			print('Off-hours...')
	# Check the time to renew/turn off the blocker every minute
	time.sleep(60)
