# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def About_page(request):
    return render(request, 'about.html')
    return redirect('home')

