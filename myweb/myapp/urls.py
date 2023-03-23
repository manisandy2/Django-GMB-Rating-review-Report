from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page,name='home_page'),
    path('store_view', store_view,name='store_view'),
    path('region', region_view,name='region'),
    path('asm_report', asm_report_view,name='asm_report'),
    path('rsm_report', rsm_report_view,name='rsm_report'),
    path('arsm_report', arsm_report_view,name='arsm_report'),
    path('drsm_report', drsm_report_view,name='drsm_report'),



]
