from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from.models import entry
from .serializers import entrySerializer, UserSerializer
from rest_framework.views import APIView
from api.smsaps import send_sms, get_code

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = entry.objects.all()
    serializer_class = entrySerializer

#webhooks

import json
from django.views.decorators.http import require_http_methods
from django.views.generic import View
from django.http import HttpResponse

#this is a webhook view that receives the json data from hubspot, once received it sends custom sms to the number
class hook_receiver_view(APIView):
    def post(self, request,*args, **kwargs):
        if True:
            send_sms(params={"msg":"Hello Fuad","to":"56968495167"})
            # print(json.loads(request.body))
            # return HttpResponse('success')


class auth_view(APIView):
    def get(self, request, *args, **kwargs):
        queryset=get_code.objects.all()
        req=request.query_params.get('code',None)
        print(req)
        if req is not None:
            return req
