# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from django.shortcuts import render, redirect

# Create your views here.
class AdminDashboardView(View):

    def get(self,request):
        return render(request, "admin_dashboard.html")



