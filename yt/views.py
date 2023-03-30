from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
#from rest_framework.decorators import api_view
from .yttrans import speech_to_text
# Create your views here.
 

# Video to audio
def speech_to_text_view(request):
   #n = request.GET.get('u')
   video_URL = request.GET.get('u')
   result = speech_to_text(video_URL)
   return JsonResponse({"transcription":result})