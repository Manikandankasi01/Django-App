from pagedown.widgets import PagedownWidget
from desg_t18.models import (
                            TriageNote, 
                            KnowledgeSharing,
                            MeetingUpdate,
                            DesgGmlUpdate,
                            DesgPcUpdate,
                            
                            )
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model,login,logout


class TriageForm(forms.ModelForm):
    sam_name=forms.CharField(max_length=50)
    content=forms.CharField(widget=PagedownWidget)
    class Meta():
        model=TriageNote
        fields =('sam_name','title','content')

    def clean(self):
        cleaned_data = super().clean()

    def get_triage_update():
        posted_data=TriageForm.objects.all()
        return posted_data

class MeetingForm(forms.ModelForm):
    title=forms.CharField(max_length=500)
    content=forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta():
        model=MeetingUpdate
        fields=('title','content')
    def clean(self):
        cleaned_data = super().clean()

class KnowledgeSharingForm(forms.ModelForm):
    answer=forms.CharField(widget=PagedownWidget(show_preview=False),required=False)
    class Meta():
        model=KnowledgeSharing
        fields=("track","question","answer")
    def clean(self):
        cleaned_data = super().clean()

class PcUpdateForm(forms.ModelForm):
    title=forms.CharField(max_length=500)
    content=forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta():
        model=DesgPcUpdate
        fields=('title','content')
    def clean(self):
        cleaned_data = super().clean()

class GmlUpdateForm(forms.ModelForm):
    title=forms.CharField(max_length=500)
    content=forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta():
        model=DesgGmlUpdate
        fields=('title','content')
    def clean(self):
        cleaned_data = super().clean()
