# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import POI
from .models import Road


admin.site.register(POI)
admin.site.register(Road)

