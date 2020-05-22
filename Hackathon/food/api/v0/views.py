from django.shortcuts import render
from food.models import (
    Food
)
from rest_framework import filters
from rest_framework import status

from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

class AllFoodViews(generics.ListCreateAPIView):
    queryset=Food.objects.all()
    serializer_class = FoodSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    def list(self,request,*args,**kwargs):
        self.object_list=self.filter_queryset(self.get_queryset())
        serializer=self.get_serializer(self.object_list,many=True)
        context={}
        data={}
        context['sucess']=True
        context['status']=200
        context['response']="sucessfull"
        context['count']=self.object_list.count()
        data=serializer.data
        context['data']=data
        return Response(context)



@api_view(['GET',])
@permission_classes((AllowAny,))
def fake(request):
    context={}
    data={}
    






    context['sucess']=True
    context['status']=200
    context['response']="sucessfull"
    
    qs=Food.objects.filter(name="Bread Chapati Or Roti Whole Wheat Commercially Prepared Frozen")
    qs=qs| Food.objects.filter(name="poha")
    qs=qs| Food.objects.filter(name="Apples")
    qs=qs| Food.objects.filter(name="Chicken Feet Boiled")

    #Chicken Feet Boiled
    context['count']=qs.count()
    serializer_class = FoodSerializer(qs,many=True)
    data=serializer_class.data
    context['data']=data
    return Response(context)

        