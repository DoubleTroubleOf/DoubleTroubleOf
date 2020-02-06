from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

<<<<<<< HEAD
=======

>>>>>>> cc523d3016ac65f43d5cfb25bd5294971430810b
def base(request):
    return render(request, 'index.html')