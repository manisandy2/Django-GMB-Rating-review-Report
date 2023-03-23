from django import forms
from .models import *


class RegionForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Region.objects.values_list('region_name',flat=True), label="Region")

    class Meta:
        model = Region
        fields = ('name',)


class ASMForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=ASM.objects.values_list('asm_name',flat=True).distinct(),label="ASM")

    class Meta:
        model = ASM
        fields = ('name',)


class RSMForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=RSM.objects.values_list('rsm_name',flat=True).distinct(),label="RSM")

    class Meta:
        model = RSM
        fields = ('name',)


class ARSMForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=ARSM.objects.values_list('arsm_name',flat=True).distinct(),label="ARSM")

    class Meta:
        model = ARSM
        fields = ('name',)


class DRSMForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=DRSM.objects.values_list('drsm_name',flat=True).distinct(),label="DRSM")

    class Meta:
        model = DRSM
        fields = ('name',)









