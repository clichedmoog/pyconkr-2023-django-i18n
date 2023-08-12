import datetime

from django.shortcuts import render

def home(request):
    request.session["django_timezone"] = "Asia/Seoul"
    now = datetime.datetime(2023, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)
    number = 1231231231.121
    context = {
        'now': now,
        'number': number,
    }
    return render(request, 'myapp/home.html', context)