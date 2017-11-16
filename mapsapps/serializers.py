from rest_framework import serializers
from .models import POI, Road, Building


class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ['id',
                  'title',
                  'location',
        ]

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = ['id',
                  'name',
                  'speed_limit',
                  'get_road_coords'
        ]

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['id',
        ]
