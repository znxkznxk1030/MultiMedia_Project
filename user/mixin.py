from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class CustomAccessMixin(AccessMixin):
    def handle_no_permission_for_authenticated_user(self):
        raise PermissionDenied


class AdminRequiredMixin(CustomAccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            if request.user.is_superuser:
                return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)
        return self.handle_no_permission_for_authenticated_user()
