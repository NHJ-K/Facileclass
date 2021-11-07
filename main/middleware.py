from datetime import timedelta as td
from django.utils import timezone
from django.conf import settings
from django.db.models.expressions import F  
from .models import teacher_info
from django.utils.deprecation import MiddlewareMixin

class LastUserActivityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        mail = request.session['mail']
        to = teacher_info.objects.get(Email=mail)
        if to.last_activity != timezone.now():
            teacher_info.objects.filter(Email=mail).update(
                last_activity=timezone.now()
            )
        return None