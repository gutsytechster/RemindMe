from datetime import timedelta

from django.utils import timezone

from src.events.email_content import EventReminder
from src.events.models import Event
from src.tasks import send_email


def send_event_reminders():
    reminder_time = timezone.now() + timedelta(minutes=15)
    events = Event.objects.filter(
        has_reminder_sent=False, set_reminder=True, scheduled_time__lte=reminder_time
    )
    for event in events:
        subject = EventReminder.subject.format(title=event.name)
        local_scheduled_time = timezone.localtime(event.scheduled_time)
        body = EventReminder.body.format(
            name=event.owner.first_name,
            title=event.name,
            date=local_scheduled_time.date().strftime("%d %b %Y"),
            time=local_scheduled_time.time().strftime("%I:%M %p"),
        )
        send_email(subject=subject, body=body, to_email=event.owner.email)
    Event.objects.filter(id__in=events).update(has_reminder_sent=True)
