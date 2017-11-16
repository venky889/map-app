# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .models import POI

# Create your views here.

class basemap(TemplateView):
	template_name='maps/base.html'


class POIView(ListView):
	model = POI
	template_name = 'maps/poi_list.html'

class POIDetail(DetailView):
	model = POI
	template_name = 'maps/poi_detail.html'
