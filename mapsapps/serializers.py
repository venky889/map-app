from rest_framework import serializers
from .models import POI, Road, Coord, Building


class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ['id',
                  'title',
                  'location',
                  'lat',
                  'lon'
        ]


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['lat', 'lon', 'sequence']


class RoadSerializer(serializers.ModelSerializer):
    coords = CoordSerializer(many=True)

    class Meta:
        model = Road
        fields = ['id',
                  'name',
                  'speed_limit',
                  'coords']


class BuildingSerializer(serializers.ModelSerializer):
    building_coords = CoordSerializer(many=True)
    class Meta:
        model = Building
        fields = ['id',
                  'name',
                  'number',
                  'coords']

