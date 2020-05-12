from apscheduler.schedulers.blocking import BlockingScheduler

from src.events.utils import send_event_reminders

sched = BlockingScheduler()


@sched.scheduled_job("interval", minutes=2)
def send_event_reminders_async():
    send_event_reminders()


try:
    sched.start()
except (KeyboardInterrupt, SystemExit):
    pass
