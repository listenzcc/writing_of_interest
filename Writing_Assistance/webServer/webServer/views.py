
import time

from django.http import HttpResponse
from django.shortcuts import render

from .worker import Worker

worker = Worker()


def index(request):
    print(request)
    contex = dict(
        CurrentTime=time.ctime()
    )
    return render(request, 'index.html', contex)


def query(request, s):
    print(request, s)
    found = worker.query(s)
    found.index = range(len(found))
    return HttpResponse(found.to_json(), content_type='application/json')
