from .models import *


class GoogleMyBusiness:
    def __init__(self,daily_data=None,region=None):
        self.daily_data = daily_data
        self.region = region

    def daily_report(self,**kwargs):
        self.daily_data = Daily_Report.objects.filter(date=kwargs.get("date"))

    def get_start_daily_report(self):
        return self.daily_data

    def run_region(self,**kwargs):
        for reg in Region.objects.all():
            # print(reg.id,reg.region_name)
            if reg.region_name == kwargs.get("reg"):
                self.region = reg.region_name

    def get_region(self):
        return self.region
