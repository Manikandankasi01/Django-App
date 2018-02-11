from pagedown.widgets import PagedownWidget
from ldm.models import (
                        LdmForum,
                        LdmMeetingUpdate,
                        )
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model, login, logout


class LdmMeetingUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=500)
    content = forms.CharField(widget=PagedownWidget(show_preview=False))

    class Meta():
        model = LdmMeetingUpdate
        fields = ('title', 'content')

    def clean(self):
        cleaned_data = super().clean()


class LdmForumForm(forms.ModelForm):
    answer = forms.CharField(widget=PagedownWidget(show_preview=False), required=False)

    class Meta():
        model = LdmForum
        fields = ("track", "question", "answer")

    def clean(self):
        cleaned_data = super().clean()

