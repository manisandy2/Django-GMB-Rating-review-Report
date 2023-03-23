from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import *
from django.db.models import Q
from .forms import *
from .GMD import GoogleMyBusiness
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegionSerializers,DailyReportSerializer
from django.http.response import JsonResponse
from django.core import serializers
import json


def home_page(request):
    return render(request,"home.html")


def store_view(request):
    if request.method == "GET":
        gmd = GoogleMyBusiness()
        gmd.daily_report(date=request.GET.get('start'))
        first_result = gmd.get_start_daily_report()
        gmd.daily_report(date=request.GET.get('end'))
        second_result = gmd.get_start_daily_report()
        results = {
            "first_results": first_result,
            "second_results": second_result,
        }
        return render(request, 'home.html',{"results": results})
    else:
        return render(request, "home.html", {})



# def store_view(request):
#     if request.method == "GET":
#         start_date = request.GET.get('start')
#         end_date = request.GET.get('end')
#
#         first_results = Daily_Report.objects.filter(Q(date__gte=start_date) & Q(date__lte=start_date))
#         second_results = Daily_Report.objects.filter(Q(date__gte=end_date) & Q(date__lte=end_date))
#         print(first_results)
#         print(second_results)
#
#         results = {
#             "first_results" : first_results,
#             "second_results" : second_results,
#             "start_date" : start_date,
#             "end_date" : end_date
#         }
#         return render(request, 'home.html',{"results": results})
#     else:
#         return render(request, "home.html", {})


def region_view(request):
    form = RegionForm()
    templates = 'region.html'
    request.GET.get('name')
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')
    # print(request.GET.get('name'))
    # print(request.GET.get('start'))
    # print(request.GET.get('end'))
    gmb = GoogleMyBusiness()
    gmb.run_region(reg=request.GET.get('name'))
    print(gmb.get_region())
    start_date_region = []
    end_date_region = []
    if request.method == 'GET':
        region = Region.objects.all()
        for r in region:
            if r.region_name == request.GET.get('name'):
                r_name = r.region_name
                st_name = STORE.objects.filter(region_id=r.id).all()
                for st in st_name:
                    master_name = st.store_name
                    dr_start = Daily_Report.objects.filter(store_id=st.id,date=start_date)
                    dr_end = Daily_Report.objects.filter(store_id=st.id,date=end_date)
                    for d in dr_start:
                        dr_list = {'region':r_name,"mname":master_name,'storename':d.store_id,'date':d.date,'rating':d.rating,'review':d.review}
                        start_date_region.append(dr_list)
                    for d in dr_end:
                        dr_list = {'region':r_name,"mname":master_name,'storename':d.store_id,'date':d.date,'rating':d.rating,'review':d.review}
                        end_date_region.append(dr_list)
                return render(request, templates, {'form': form,'start_region': start_date_region,'end_region': end_date_region})
    return render(request, templates, {'form': form})


def asm_report_view(request):
    fm = ASMForm()
    start_date_region = []
    end_date_region = []
    templates = "asm.html"
    if request.method == "GET":
        asm_filter = ASM.objects.filter(asm_name=request.GET.get("name"))
        for asm in asm_filter:
            # st_name = STORE.objects.filter(store_name=asm.store_id).all()
            dr_start = Daily_Report.objects.filter(store_id=asm.store_id, date=request.GET.get('start'))
            dr_end = Daily_Report.objects.filter(store_id=asm.store_id, date=request.GET.get('end'))
            for d in dr_start:
                dr_list = {'asm':request.GET.get("name"),'storename': d.store_id, 'date': d.date,'rating': d.rating, 'review': d.review}
                start_date_region.append(dr_list)
            for d in dr_end:
                dr_list = {"asm": request.GET.get("name"), 'storename': d.store_id, 'date': d.date,'rating': d.rating, 'review': d.review}
                end_date_region.append(dr_list)
        return render(request,templates,{"form":fm,'start_region': start_date_region,'end_region': end_date_region})
    return render(request,templates,{"form":fm})


def rsm_report_view(request):
    fm = RSMForm()
    start_date_region = []
    end_date_region = []
    templates = "rsm.html"
    if request.method == "GET":
        asm_filter = RSM.objects.filter(rsm_name=request.GET.get("name"))
        for asm in asm_filter:
            # st_name = STORE.objects.filter(store_name=asm.store_id).all()
            dr_start = Daily_Report.objects.filter(store_id=asm.store_id, date=request.GET.get('start'))
            dr_end = Daily_Report.objects.filter(store_id=asm.store_id, date=request.GET.get('end'))
            for d in dr_start:
                dr_list = {'rsm':request.GET.get("name"),'storename': d.store_id, 'date': d.date,'rating': d.rating, 'review': d.review}
                start_date_region.append(dr_list)
            for d in dr_end:
                dr_list = {"rsm": request.GET.get("name"), 'storename': d.store_id, 'date': d.date,'rating': d.rating, 'review': d.review}
                end_date_region.append(dr_list)
        return render(request,templates,{"form":fm,'start_region': start_date_region,'end_region': end_date_region})
    return render(request,templates,{"form":fm})


def arsm_report_view(request):
    fm = ARSMForm()
    start_date_region = []
    end_date_region = []
    templates = "arsm.html"
    if request.method == "GET":
        rsm_filter = ARSM.objects.filter(arsm_name=request.GET.get("name"))
        for rsm in rsm_filter:
            dr_start = Daily_Report.objects.filter(store_id=rsm.store_id, date=request.GET.get('start'))
            dr_end = Daily_Report.objects.filter(store_id=rsm.store_id, date=request.GET.get('end'))
            for d in dr_start:
                dr_list = {'arsm':request.GET.get("name"),'storename': d.store_id, 'date': d.date,'rating': d.rating, 'review': d.review}
                start_date_region.append(dr_list)
            for d in dr_end:
                dr_list = {"arsm": request.GET.get("name"), 'storename': d.store_id, 'date': d.date,'rating': d.rating, 'review': d.review}
                end_date_region.append(dr_list)
        return render(request,templates,{"form":fm,'start_region': start_date_region,'end_region': end_date_region})
    return render(request,templates,{"form":fm})


def drsm_report_view(request):
    fm = DRSMForm()
    start_date_region = []
    end_date_region = []
    templates = "drsm.html"
    if request.method == "GET":
        drsm_filter = DRSM.objects.filter(drsm_name=request.GET.get("name"))
        for drsm in drsm_filter:
            dr_start = Daily_Report.objects.filter(store_id=drsm.store_id, date=request.GET.get('start'))
            dr_end = Daily_Report.objects.filter(store_id=drsm.store_id, date=request.GET.get('end'))
            for d in dr_start:
                dr_list = {'drsm':request.GET.get("name"),'storename': d.store_id, 'date': d.date,'rating': d.rating, 'review': d.review}
                start_date_region.append(dr_list)
            for d in dr_end:
                dr_list = {"drsm": request.GET.get("name"), 'storename': d.store_id, 'date': d.date,'rating': d.rating, 'review': d.review}
                end_date_region.append(dr_list)
        return render(request,templates,{"form":fm,'start_region': start_date_region,'end_region': end_date_region})
    return render(request,templates,{"form":fm})
