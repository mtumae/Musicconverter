from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Mxl_files, Tester_table


class mxl_files(forms.ModelForm):  
    class Meta:
        model = Mxl_files
        fields = "__all__"


class Tester(forms.ModelForm):  
    class Meta:
        model = Tester_table
        fields = "__all__"
