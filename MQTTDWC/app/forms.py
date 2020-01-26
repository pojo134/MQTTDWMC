"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from app.models import Message
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class NewMessageForm(forms.Form):
    topic = forms.CharField(max_length=50,
                            widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Topic'}))
    message_string = forms.CharField(max_length=100,
                                     widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': 'Message'}))