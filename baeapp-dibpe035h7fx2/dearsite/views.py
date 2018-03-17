# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AddForm


def index(request):
    if request.method == 'POST':

        form = AddForm(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:
        form = AddForm()
    return render(request, 'dearsite/index.html', {'form': form})


def myhomeweb(request):
    return render(request, 'dearsite/myhomeweb.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


from django.conf import settings
from django.core.mail import send_mail


def send(request):
    msg = '<a href="http://www.baidu.com" target="_blank">sdsa</a>'
    send_mail('test', 'Hello', settings.EMAIL_FROM, ['feihu126@163.com'], fail_silently=False)
    return HttpResponse('ok')
