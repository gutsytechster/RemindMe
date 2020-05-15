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


class ValidateRegister:

    subject = "[Remind Me] Verify Email Registration"
    body = (
        """ Dear {name},

Thank you for signing up. You can use the following link to complete your verified \
registration and get started on our platform:

"""
        + settings.PLATFORM_URL
        + """?action=signup&token={token}

If you need any assistance or have any questions, please feel free to reach out.

Regards,
Team RemindMe

    """
    )
