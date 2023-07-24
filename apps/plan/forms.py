# @Time   : 2018/9/29 11:18
# @Author : RobbieHan
# @File   : forms.py

from django import forms
from .models import DailySchedule


class DailyScheduleForm(forms.ModelForm):
    class Meta:
        model = DailySchedule
        fields = '__all__'
