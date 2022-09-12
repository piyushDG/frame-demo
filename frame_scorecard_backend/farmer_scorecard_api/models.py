from django.db import models

# Create your models here.

def auto_str(cls):
    def __str__(self):
        return "%s(%s)" % (
            type(self).__name__,
            ", ".join("%s=%s" % item for item in vars(self).items()),
        )

    cls.__str__ = __str__
    return cls

@auto_str
class Kharif1Paddy2021_one(models.Model):
    id = models.BigIntegerField(primary_key=True)
    farmer_name = models.CharField(max_length=255, blank=True, null=True)
    #gaurdian_name_field = models.CharField(db_column='gaurdian_name ', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gaurdian_name = models.CharField(max_length=255, blank=True, null=True)
    #mobile_numbe_field = models.CharField(db_column='mobile_numbe ', max_length=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    village_name = models.CharField(max_length=255, blank=True, null=True)
    total_land = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    previous_crop_name = models.CharField(max_length=255, blank=True, null=True)
    previous_harvest_date = models.DateField(blank=True, null=True)
    area_previous_crop = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    #date_chemical_fertilizer_field = models.DateField(db_column='date_chemical_fertilizer ', blank=True, null=True) # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date_chemical_fertilizer = models.DateField(blank=True, null=True)
    qty_urea_46 = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    qty_dap_18_46_0 = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    qty_fertilizers_12_12_12 = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    qty_fertilizer_20_20_0_13 = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    amount_manure_mop = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    apply_spraying = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    #apply_fertilizing_roots = models.DecimalField(db_column='apply_Fertilizing_roots', max_digits=255, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    apply_fertilizing_roots = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    date_cattelmanure_fertilizer = models.DateField(blank=True, null=True)
    cattelmanure_fertilizer_name = models.CharField(max_length=255, blank=True, null=True)
    qty_cattelmanure_fertilizer = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    manure_soil_topping = models.CharField(max_length=255, blank=True, null=True)
    date_apply_ghanamrit = models.DateField(blank=True, null=True)
    qty_greenmanure_ghanamrit = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    crop_name = models.CharField(max_length=255, blank=True, null=True)
    area_farm = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    qty_urea_utilization_46 = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    date_urea_use = models.DateField(blank=True, null=True)
    #number_2_qty_dap_use_18_46_0 = models.DecimalField(db_column='2_qty_dap_use_18_46_0', max_digits=255, decimal_places=7, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    #number_2_date_dap_18_46_0 = models.DateField(db_column='2_date_dap_18_46_0', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    #number_2_qty_use_20_20_0_13 = models.DecimalField(db_column='2_qty_use_20_20_0_13', max_digits=255, decimal_places=7, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    #number_2_date_access_data_20_20_0_13 = models.DateField(db_column='2_date_access_data_20_20_0_13', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2_qty_dap_use_18_46_0 = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2_date_dap_18_46_0 = models.DateField(blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2_qty_use_20_20_0_13 = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2_date_access_data_20_20_0_13 = models.DateField(blank=True, null=True)
    scr_irrigation = models.CharField(max_length=255, blank=True, null=True)
    method_irrigation = models.CharField(max_length=255, blank=True, null=True)
    natural_remedies = models.CharField(max_length=255, blank=True, null=True)
    date_greenmanure_jeevamrut = models.DateField(blank=True, null=True)
    qty_greenmanure_jeevamrut = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    date_greenmanure_jeevamrut_2 = models.DateField(blank=True, null=True)
    qty_greenmanure_jeevamrut_2 = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    date_harvest = models.DateField(blank=True, null=True)
    cost_manual_labor_perkatta = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    date_threshing = models.DateField(blank=True, null=True)
    harvest_paddy_yield = models.CharField(max_length=255, blank=True, null=True)
    yield_perkatta = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    total_yield = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    avg_height_plant_before_harvesting = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    height_stalk_lft_after_harvesting_crop = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    date_plowing_back_into_soil = models.DateField(blank=True, null=True)
    date_sowing = models.DateField(blank=True, null=True)
    nursery_sowing_date = models.DateField(blank=True, null=True)
    date_planting_field = models.DateField(blank=True, null=True)
    plowing_the_field = models.DateField(blank=True, null=True)
    depth_of_tillage = models.DecimalField(max_digits=255, decimal_places=7, blank=True, null=True)
    irrigation_date_borewell = models.DateField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'kharif1_paddy_2021'