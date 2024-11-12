
from plyer import notification

def notify_user(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

    
    
notify_user("Reminder","It's time to take a break")