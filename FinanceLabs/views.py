from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def base(request):
    return render(request, 'index.html')