from django.db import models


# Create your models here.

class Region(models.Model):
    region_name = models.CharField(max_length=120)

    def __str__(self):
        return self.region_name

    class Meta:
        db_table = "Region"
        verbose_name_plural = "Region"


class STORE(models.Model):
    region_id = models.ForeignKey(to=Region, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)

    def __str__(self):
        # return '%s %s' % (self.name, self.region.name)
        return self.store_name

    class Meta:
        db_table = "Store"
        verbose_name_plural = "Store"


class ASM(models.Model):
    region_id = models.ForeignKey(to=Region,on_delete=models.CASCADE)
    store_id = models.ForeignKey(to=STORE,on_delete=models.CASCADE)
    asm_name = models.CharField(max_length=255,blank=True,null=True,unique=False)

    def __str__(self):
        return self.region_id.region_name

    class Meta:
        db_table = "ASM"
        verbose_name_plural = "ASM"


class RSM(models.Model):
    region_id = models.ForeignKey(to=Region,on_delete=models.CASCADE)
    store_id = models.ForeignKey(to=STORE, on_delete=models.CASCADE)
    rsm_name = models.CharField(max_length=255,blank=True,null=True,unique=False)

    def __str__(self):
        return self.region_id.region_name

    class Meta:
        db_table = "RSM"
        verbose_name_plural = "RSM"


class ARSM(models.Model):
    region_id = models.ForeignKey(to=Region,on_delete=models.CASCADE)
    store_id = models.ForeignKey(to=STORE, on_delete=models.CASCADE)
    arsm_name = models.CharField(max_length=255,blank=True,null=True,unique=False)

    def __str__(self):
        return self.region_id.region_name

    class Meta:
        db_table = "ARSM"
        verbose_name_plural = "ARSM"


class DRSM(models.Model):
    region_id = models.ForeignKey(to=Region,on_delete=models.CASCADE)
    store_id = models.ForeignKey(to=STORE, on_delete=models.CASCADE)
    drsm_name = models.CharField(max_length=255,blank=True,null=True,unique=False)

    def __str__(self):
        return self.region_id.region_name

    class Meta:
        db_table = "DRSM"
        verbose_name_plural = "DRSM"


class Daily_Report(models.Model):
    store_id = models.ForeignKey(to=STORE, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    rating = models.FloatField(blank=True,null=True,unique=False)
    review = models.IntegerField(blank=True,null=True,unique=False)

    def __str__(self):
        return self.store_id.store_name

    class Meta:
        db_table = "Daily_Report"
        verbose_name_plural = "Daily Report"


class DailyMessageReport(models.Model):
    date = models.DateField(auto_now_add=True)
    store_id = models.ForeignKey(to=STORE, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255,blank=True,null=True,unique=False)
    customer_rating = models.IntegerField(blank=True,null=True,unique=False)
    customer_message = models.TextField(blank=True,null=True,unique=False)
    status = models.CharField(max_length=255,blank=True,null=True,unique=False)
    reply_or_no_replay = models.CharField(max_length=255,blank=True,null=True,unique=False)
    hours = models.DateField()
    get_text = models.CharField(max_length=255,blank=True,null=True,unique=False)
    replay_message = models.TextField(blank=True,null=True,unique=False)

    def __str__(self):
        return self.store_id.store_name

    class Meta:
        db_table = "Daily_Message_Report"
        verbose_name_plural = "Daily Message Report"



