from django.forms import ModelForm
from .models import *

class stud_form(ModelForm):

    class Meta:
        model=Student
        # fields=['name','location']
        fields="__all__"


