from dataclasses import fields
import imp
from statistics import mode
from django import forms
from .models import Department,Book
class deptform(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'

class newbook(forms.ModelForm):
    class Meta:
        model=Book
        exclude={'dept'}