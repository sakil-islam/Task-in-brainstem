from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from user_info import models
from user_info import forms
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.db.models import Q

import user_info


# Create your views here.
@login_required
def home(request):

    diction = {}
    return render(request, 'user_info/home.html', context=diction)
