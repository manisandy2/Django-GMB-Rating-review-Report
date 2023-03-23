from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources


@admin.register(Region)
class AdminRegion(ImportExportModelAdmin):
    fields = ('region_name',)
    list_display = ('id',"region_name",)


@admin.register(STORE)
class AdminStoreName(ImportExportModelAdmin):
    fields = ('region_id','store_name',)
    list_display = ('region_id','store_name')


@admin.register(ASM)
class AdminASM(ImportExportModelAdmin):
    fields = ('region_id','asm_name','store_id')
    list_display = ('region_id','asm_name','store_id')


@admin.register(ARSM)
class AdminARSM(ImportExportModelAdmin):
    fields = ('region_id','arsm_name','store_id')
    list_display = ('region_id','arsm_name','store_id')


@admin.register(DRSM)
class AdminDRSM(ImportExportModelAdmin):
    fields = ('region_id','drsm_name','store_id')
    list_display = ('region_id','drsm_name','store_id')


@admin.register(RSM)
class AdminRSM(ImportExportModelAdmin):
    fields = ('region_id','rsm_name','store_id')
    list_display = ('region_id','rsm_name','store_id')


@admin.register(Daily_Report)
class AdminStoreName(ImportExportModelAdmin):
    fields = ('store_id','date','rating','review')
    list_display = ('date','store_id','rating','review')


@admin.register(DailyMessageReport)
class AdminDailyMessageReport(ImportExportModelAdmin):
    fields = ('store_id','customer_name','customer_rating','customer_message','status','reply_or_no_replay','hours','get_text','replay_message')
    list_display = ('date','store_id','customer_name','customer_rating','customer_message','status','reply_or_no_replay','hours','get_text','replay_message')

