# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here. 
class Coordinate(models.Model):
    x = models.DecimalField(max_digits=9, decimal_places=6)
    y = models.DecimalField(max_digits=9, decimal_places=6)
 
    def __repr__(self):
        return "Coordinate({}, {})".format(x, y)
 
    def location(self):
        return (x, y)
 
 
class POI(models.Model):
    title = models.CharField(max_length=255, unique=True)
    location = models.ForeignKey('Coordinate')
 
    def __str__(self):
        return "{title} at ({x}, {y})".format(title=self.title,
                                             x=self.location.x,
                                             y=self.location.y)
 
class Road(models.Model):
    name = models.CharField(max_length=255, unique=True)
    speed_limit = models.IntegerField()
 
    def starts_at(self):
        self.RoadCood_set.all().order_by('sequence').first()
 
    def ends_at(self):
        self.RoadCood_set.all().order_by('-sequence').first()
 
    def get_road_coords(self):
        self.RoadCood_set.all().order_by('sequence')
 
    def __str__(self):
        return "{name}/{sl} starts at {start}".format(name=self.name,
                                                      sl=self.speed_limit,
                                                      start=self.starts_at.location)
 
 
class RoadCoord(models.Model):
    road = models.ForeignKey('Road')
    coordinate = models.ForeignKey('Coordinate')
    # To help us build the road, pt1, pt2, pt3, etc
    sequence = models.IntegerField()
 
    class Meta:
        unique_together = ['road', 'sequence']
 
 
class Building(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    coord_1 = models.ForeignKey('Coordinate', related_name='coord_1')
    coord_2 = models.ForeignKey('Coordinate', related_name='coord_2')
    coord_3 = models.ForeignKey('Coordinate', related_name='coord_3')
    coord_4 = models.ForeignKey('Coordinate', related_name='coord_4')
 
    def __str__(self):
        return "Bldg {num}: {name} at {coord}".format(num=self.number,
                                                      name=self.name,
                                                      coord=self.coord_1.location)
 
    def get_building_outline(self):
        return [coord_1, coord_2, coord_3, coord_4]