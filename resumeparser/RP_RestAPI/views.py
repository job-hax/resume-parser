from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
import json
import random

import requests
from rest_framework.parsers import JSONParser
from RP_RestAPI.parser import parse
from django.core.files.storage import FileSystemStorage

# Create your views here.

@require_POST
@csrf_exempt
def resume_parser(request):
    my_uploaded_file = request.FILES['resume']
    json = parse(my_uploaded_file)
    return JsonResponse(json, safe=False)