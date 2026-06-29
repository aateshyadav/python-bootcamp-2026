import time
from plyer import notification

while True:
    print("Please sip some water")
    notification.notify(title="please drink some water",
                        message="your need to drink some water")
    time.sleep(60*60)