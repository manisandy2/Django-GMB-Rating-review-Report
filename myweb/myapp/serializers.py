from rest_framework import serializers
from .models import Region,Daily_Report


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id','name']


class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_Report
        fields = ['id','store_name','date','rating','review']