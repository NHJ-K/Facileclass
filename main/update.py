
from apscheduler.schedulers.background import BackgroundScheduler
from .models import user_info,teacher_info
import datetime


def start():
    scheduler = BackgroundScheduler()
    scheduler2 = BackgroundScheduler()
    scheduler.add_job(ls, 'cron', hour='22')
    scheduler2.add_job(toekndelete, 'interval', minutes=3600)
    scheduler.start()
    scheduler2.start()

def toekndelete():
    infou=user_info.objects.all()
    infot=teacher_info.objects.all()
    for l in infou:
        l.token=None
    for l in infot:
        l.token=None



def ls():
    if user_info.objects.filter(Activate=False).exists():
        ls=user_info.objects.filter(Activate=False)
        for l in ls:
            coh=int(datetime.datetime.now().strftime('%H'))
            cod=int(datetime.datetime.now().strftime('%d'))
            crh=int(l.created_at.strftime('%H'))
            crd=int(l.created_at.strftime('%d'))
            if cod<crd:
                if coh<crh:
                    ls.delete()
                elif cod+1<crd:
                    ls.delete()

    if teacher_info.objects.filter(Activate=False).exists():
        ls=teacher_info.objects.filter(Activate=False)
        for l in ls:
            coh=int(datetime.datetime.now().strftime('%H'))
            cod=int(datetime.datetime.now().strftime('%d'))
            crh=int(l.created_at.strftime('%H'))
            crd=int(l.created_at.strftime('%d'))
            if cod<crd:
                if coh<crh:
                    ls.delete()
                elif cod+1<crd:
                    ls.delete()






