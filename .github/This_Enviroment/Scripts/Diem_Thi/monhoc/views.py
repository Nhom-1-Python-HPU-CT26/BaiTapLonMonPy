from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def monhoc(request):
    template = loader.get_template('mon1.html')
    return HttpResponse(template.render())