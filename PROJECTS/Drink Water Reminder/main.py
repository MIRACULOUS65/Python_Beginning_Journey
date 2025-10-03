import time
from plyer import notification


while True:
    print("Time to drink water!")
    notification.notify(title="please drink some water",message="u need to drink h2o")
    time.sleep(3)  # Remind every hour

# Note: This is a simple console-based reminder. For a more advanced application, consider using notifications or a GUI.