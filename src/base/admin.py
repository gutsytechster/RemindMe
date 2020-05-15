from django.contrib import admin
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


class CustomOutstandingTokenAdmin(OutstandingTokenAdmin):

    def has_delete_permission(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return True
        return False


admin.site.unregister(OutstandingToken)
admin.site.register(OutstandingToken, CustomOutstandingTokenAdmin)
