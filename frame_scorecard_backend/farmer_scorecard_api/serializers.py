from rest_framework import serializers
from .models import Kharif1Paddy2021_one
from django.db.models.functions import Greatest
from django.db.models import Max
class Kharif1Paddy2021Serializer(serializers.ModelSerializer):
    land_area = serializers.SerializerMethodField()
    
    class Meta:
        model = Kharif1Paddy2021_one
        fields = ('id','farmer_name','gaurdian_name', 'mobile_number','land_area','village_name','qty_urea_46','qty_dap_18_46_0','area_farm',
                  'qty_urea_utilization_46','number_2_qty_dap_use_18_46_0','yield_perkatta','total_yield')
    
    def get_land_area(self, obj):
        return Max(obj.total_land, obj.area_farm)
        