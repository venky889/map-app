# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
 
 
class POI(models.Model):
    title = models.CharField(max_length=255, unique=True)
    location = GeopositionField()
 
    def __str__(self):
        return "{title} at ({x}, {y})".format(title=self.title,
                                             x=self.location.latitude,
                                             y=self.location.longitude)
 
class Road(models.Model):
    name = models.CharField(max_length=255, unique=True)
    speed_limit = models.IntegerField()
 
    def starts_at(self):  #start line
        self.RoadCood_set.all().order_by('sequence').first()
 
    def ends_at(self):       #end line
        self.RoadCood_set.all().order_by('-sequence').first()
 
    def get_road_coords(self):    #return list of all the road coordinates
        self.RoadCood_set.all().order_by('sequence')
 
    def __str__(self):
        return "{name}/{sl} starts at {start}".format(name=self.name,
                                                      sl=self.speed_limit,
                                                      start=self.starts_at.location)
 
 
class RoadCoord(models.Model):
    road = models.ForeignKey('Road')
    coordinate = GeopositionField()
    # To help us build the road, pt1, pt2, pt3, etc
    sequence = models.IntegerField()
 
    class Meta:
        unique_together = ['road', 'sequence']
 
 
class Building(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    coord_1 = GeopositionField()
    coord_2 = GeopositionField()
    coord_3 = GeopositionField()
    coord_4 = GeopositionField()
 
    def __str__(self):
        return "Bldg {num}: {name} at {coord}".format(num=self.number,
                                                      name=self.name,
                                                      coord=self.coord_1.location)
 
    def get_building_outline(self):
        return [coord_1, coord_2, coord_3, coord_4]