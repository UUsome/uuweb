from django import forms
from .models import TypeDetail,Frame,Solution


class TypeForm(forms.ModelForm):
    class Meta:
        model = TypeDetail
        fields = ('level','p_type_id','name')


class FrameForm(forms.ModelForm):
    class Meta:
        model = Frame
        fields = ('type_id','order_flage','name')


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ('range_flage', 'frame_id', 'name')

