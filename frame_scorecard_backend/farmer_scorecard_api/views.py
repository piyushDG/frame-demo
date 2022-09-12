from django.shortcuts import render
from rest_framework import generics, status, views , viewsets
from rest_framework.response import Response
from django.conf import settings
from .models import Kharif1Paddy2021_one
from farmer_scorecard_api.serializers import Kharif1Paddy2021Serializer
from django.db.models.functions import Greatest
class Kharif1Paddy2021_oneViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Kharif1Paddy2021_one.objects.all()
    serializer_class = Kharif1Paddy2021Serializer
    
    def list(self, request):
        queryset = self.get_object()
        print(queryset)
        serializer = self.get_serializer(data=queryset,many=True)
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        #queryset = self.get_object()
        queryset = Kharif1Paddy2021_one.objects.filter(mobile_number=pk).all()
        #land_area_qs = Kharif1Paddy2021_one.objects.annotate(land_area=Greatest('total_land','area_farm')).filter(mobile_number=pk).order_by('land_area')
        #average_urea = Kharif1Paddy2021_one.objects.
        #print(land_area_qs['land_area'])
        
        serializer = Kharif1Paddy2021Serializer(queryset,many=True)
    
        return Response(serializer.data)

