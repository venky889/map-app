# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import POI, Road, Building
from .serializers import POISerializer, RoadSerializer, BuildingSerializer




# Create your views here.

class basemap(TemplateView):
	template_name='maps/map.html'


class POIView(ListView):
	model = POI
	template_name = 'maps/poi_list.html'

class POIDetail(DetailView):
	model = POI
	template_name = 'maps/poi_detail.html'


##### API VIEWS ####
class POIViewSet(viewsets.ModelViewSet):
    queryset = POI.objects.all()
    serializer_class = POISerializer


class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

