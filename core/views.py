# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
class LogInView(View):

    def get(self,request):
        return render(request, "login.html")

    def post(self, request):
        print request.POST
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/dashboard")

class LogOutView(View):

    def get(self, request):
        print request.user
        logout(request)
        return render(request, "login.html")

class ChartsView(View):

    def get(self, request):
        return render(request, "master/chart.html")


