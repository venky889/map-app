"""mapproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from mapsapps.views import (
    basemap,
    POIView,
    POIDetail,
    POIViewSet,
    RoadViewSet,
    BuildingViewSet,
)
from mapproject.views import HomePage


router = routers.SimpleRouter()
router.register(r'poi', POIViewSet, base_name='poi')
router.register(r'road', RoadViewSet, base_name='road')
router.register(r'building', BuildingViewSet, base_name='building')



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^map/$', basemap.as_view(), name="map"),
    # url(r'^basemap/', basemap.as_view(), name="map2"),
    url(r'^poi/$', POIView.as_view(), name='poi_list'),
    url(r'^poi/(?P<pk>\d+)/$', POIDetail.as_view(), name='poi_detail'),
]
