from django.core.exceptions import PermissionDenied


class OwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author_id != request.user.id:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
