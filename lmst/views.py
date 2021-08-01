from django.shortcuts import render
def page_not_found_view(request, exception):
    return render(request, 'error/404.html', status=404)

def handler(request,*args, **kwargs):
    return render(request, 'error/500.html', status=500)