from automation.models import (
                            DesgAutomationUpdate,
                            DesgAutomationRelease,
                            PdcAutomationUpdate,
                            PdcAutomationRelease,
                            LdmAutomationUpdate,
                            LdmAutomationRelease,
                            )
from django import forms
from pagedown.widgets import PagedownWidget
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model,login,logout

'''
DESG From
'''
class DesgAutomationUpdateForm(forms.ModelForm):
    title=forms.CharField(max_length=500)
    content=forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta():
        model=DesgAutomationUpdate
        fields=('title','content')
    def clean(self):
        cleaned_data = super().clean()

class DesgAutomationReleaseNoteForm(forms.ModelForm):
    title=forms.CharField(max_length=500)
    content=forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta():
        model=DesgAutomationRelease
        fields=('title','content')
    def clean(self):
        cleaned_data = super().clean()


'''
PDC Form
'''
class PdcAutomationUpdateForm(forms.ModelForm):
    title=forms.CharField(max_length=500)
    content=forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta():
        model=PdcAutomationUpdate
        fields=('title','content')
    def clean(self):
        cleaned_data = super().clean()

class PdcAutomationReleaseNoteForm(forms.ModelForm):
    title=forms.CharField(max_length=500)
    content=forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta():
        model=PdcAutomationRelease
        fields=('title','content')
    def clean(self):
        cleaned_data = super().clean()

'''
LDM Forms
'''

class LdmAutomationUpdateForm(forms.ModelForm):
    title=forms.CharField(max_length=500)
    content=forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta():
        model=LdmAutomationUpdate
        fields=('title','content')
    def clean(self):
        cleaned_data = super().clean()

class LdmAutomationReleaseNoteForm(forms.ModelForm):
    title=forms.CharField(max_length=500)
    content=forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta():
        model=LdmAutomationRelease
        fields=('title','content')
    def clean(self):
        cleaned_data = super().clean()