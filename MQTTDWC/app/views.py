"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from app.forms import NewMessageForm
from django.http import HttpRequest
from app.models import Message
from django.views.generic import ListView

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

class topic_list(ListView):
    model = Message


def publish(request):
    """Renders the about page."""
    if request.method == "POST":
            form = NewMessageForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.timestamp = timezone.now()
                model_instance.save()
                return redirect('/topics')
 
    else:
        form = NewMessageForm() 
        return render(request, "app/publish.html", {'form': form})
