from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.
def formgen(req):
  calltime = datetime.datetime.now()
  img = None
  
  formlink = ''
  res = {
    "formlink": "",
    "fields": {

    },
    "formpng": img
  }
  return HttpResponse(res)