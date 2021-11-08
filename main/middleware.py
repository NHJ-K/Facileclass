from django.utils import timezone
from .models import teacher_info

def process_request(request):
    mail = request.session['mail']
    to = teacher_info.objects.get(Email=mail)
    if to.last_activity != timezone.now():
        teacher_info.objects.filter(Email=mail).update(
            last_activity=timezone.now()
        )
        return None