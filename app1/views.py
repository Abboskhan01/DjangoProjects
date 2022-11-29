from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# def my_view(request):
#     output = _("Welcome to my site.")
#     return HttpResponse(output)
# # Create your views here.
from django.http import HttpResponse
from django.utils.translation import gettext


def my_view(request):
    output = gettext("Welcome to my site.")
    return HttpResponse(output)
