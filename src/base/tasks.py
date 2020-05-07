from django.conf import settings
from django.core.mail import send_mail

from src.celery_app import app


@app.task
def send_email(subject, body, to_email, from_email=settings.EMAIL_HOST_USER):
    send_mail(
        subject=subject,
        message=body,
        from_email=from_email,
        recipient_list=[to_email],
        fail_silently=False,
    )
