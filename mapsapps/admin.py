# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import POI, Road, Coord, Building


admin.site.register(POI)
admin.site.register(Road)
admin.site.register(Coord)
admin.site.register(Building)

