from django.conf import settings


class PasswordReset:

    subject = "Password Reset Mail"
    body = (
        """ Dear {name},

You have just requested a password reset for our application.
Please click on the following link for setting up a new password.

"""
        + settings.PLATFORM_URL
        + """?action=reset_password&token={token}

Regards,
Team RemindMe
    """
    )
