from pagedown.widgets import PagedownWidget
from pdc.models import (
                        PdcForum,
                        PdcMeetingUpdate,


)
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model, login, logout


class PdcMeetingUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=500)
    content = forms.CharField(widget=PagedownWidget(show_preview=False))

    class Meta():
        model = PdcMeetingUpdate
        fields = ('title', 'content')

    def clean(self):
        cleaned_data = super().clean()


class PdcForumForm(forms.ModelForm):
    answer = forms.CharField(widget=PagedownWidget(show_preview=False), required=False)

    class Meta():
        model = PdcForum
        fields = ("track", "question", "answer")

    def clean(self):
        cleaned_data = super().clean()

