# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from django.shortcuts import render, redirect

# Create your views here.
class DashboardView(View):

    def get(self,request):
        return render(request, "dashboard.html")



