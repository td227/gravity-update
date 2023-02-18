import schedule
import time
import subprocess

def update_gravity():
    subprocess.call(['pihole', '-g'])

schedule.every().day.at('02:00').do(update_gravity)

while True:
    schedule.run_pending()
    time.sleep(60)