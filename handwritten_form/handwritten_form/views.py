import datetime, json, base64, os

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from PIL import Image

from .src import form_generate

# Step 1: Form generation
class FormGen(View):

  def get(self,req):
    return HttpResponse('Send POST request for security pls')
  
  @csrf_exempt
  def post(self,req):
    data = json.loads(req.body.decode('utf-8'))
    formname = data['formname']+'.png'
    fields = data['fields']
    form_generate.generate_form(formname,fields)
    loc = os.path.join(os.path.join(os.getcwd(),'data'),formname)
    print("LOCATION:",loc)
    imgfile = open(loc,'rb')
    return HttpResponse(imgfile.read(),content_type='image/png')

  # DANGEROUS
  @csrf_exempt
  def dispatch(self, *args, **kwargs):
    return super(FormGen, self).dispatch(*args, **kwargs)

# Step 2: Image Analysis
class ImgAnal(View):

  def get(self,req):
    return HttpResponse('Send POST request for security pls')
  
  '''
  req items -

  '''
  @csrf_exempt
  def post(self,req):
    return HttpResponse('still doing.. chill!')

  # DANGEROUS
  @csrf_exempt
  def dispatch(self, *args, **kwargs):
    return super(FormGen, self).dispatch(*args, **kwargs)