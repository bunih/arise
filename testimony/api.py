from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import TestimonySerializer
from rest_framework.views import APIView


class ItemList(APIView):
    def get(self, request, format=None):
        events = Testimony.objects.all()
        serializer = TestimonySerializer(events, many=True)
        return Response(serializer.data)
        
    def post(self,*args,**kwargs ):
        print(self.request.data)
        events=Testimony.objects.create(**self.request.data)
        return Response({'events':'events'})

    def delete(self,*args,**kwargs):
        print(self.request.data)
        print(self.kwargs.get('id'))
        print('deleting....')
        Testimony.objects.filter(id=self.kwargs.get('id')).delete()
        return Response({'events':'new'})