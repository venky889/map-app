# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from geoposition.fields import GeopositionField


class POI(models.Model):
    title = models.CharField(max_length=255, unique=True)
    location = GeopositionField()

    def __str__(self):
        return "{title} at ({x}, {y})".format(title=self.title,
                                             x=self.location.latitude,
                                             y=self.location.longitude)

    @property
    def lat(self):
        return self.location.latitude

    @property
    def lon(self):
        return self.location.longitude


class Road(models.Model):
    name = models.CharField(max_length=255, unique=True)
    speed_limit = models.IntegerField()

    @property
    def starts_at(self):  #start line
        return self.coords.all().order_by('sequence').first()

    @property
    def ends_at(self):       #end line
        return self.coords.all().order_by('-sequence').first()

    @property
    def coords(self):
        return self.road_coords.all().order_by('sequence')

    def get_next_sequence(self):
        if self.coords:
            return self.road_coords.last().sequence + 1
        else:
            return 1

    def __str__(self):
        name_str = "{name}/{sl}".format(name=self.name,
                                        sl=self.speed_limit)

        if self.coords:
            starts_str = " starts at {}".format(self.starts_at.location)
            name_str += starts_str

        return name_str



class Building(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "Bldg {num}: {name}".format(num=self.number,
                                           name=self.name)

    @property
    def starts_at(self):
        return self.coords.all().order_by('sequence').first()

    @property
    def coords(self):
        return self.building_coords.all().order_by('sequence')

    def get_next_sequence(self):
            if self.coords:
                return self.building_coords.last().sequence + 1
            else:
                return 1

    def __str__(self):
        name_str = "{name}/{number}".format(name=self.name,
                                            number=self.number)

        if self.coords:
            starts_str = " starts at {}".format(self.starts_at.location)
            name_str += starts_str
        return name_str


class CoordManager(models.Manager):
    def safe_get(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None

class Coord(models.Model):
    road = models.ForeignKey('Road', related_name='road_coords',
                             null=True, blank=True, on_delete=models.CASCADE)
    building = models.ForeignKey('Building', related_name='building_coords',
                                 blank=True, null=True, on_delete=models.CASCADE)
    location = GeopositionField()
    sequence = models.IntegerField(blank=True)

    objects = CoordManager()

    @property
    def lat(self):
        return self.location.latitude

    @property
    def lon(self):
        return self.location.longitude

    class Meta:
        unique_together = (('road', 'sequence'),
                           ('building', 'sequence'))

    def __str__(self):
        if self.road:
            name = self.road.name
        elif self.building:
            name = self.building.name
        else:
            raise Exception("Each Point shoudl belong to a Road or Building")
        return "Point {} of {} at ({}, {})".format(self.sequence,
                                                   name,
                                                   self.lat,
                                                   self.lon)


@receiver(pre_save, sender=Coord)
def coord_callback(sender, instance, *args, **kwargs):
    if instance.road:
        instance.sequence = instance.road.get_next_sequence()
    elif instance.building:
        instance.sequence = instance.building.get_next_sequence()
    else:
        raise Exception("Can't have a Point without Building or Road")
