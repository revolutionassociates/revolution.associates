"""URLs of the DIRECT track (statutory, challans, payroll processing, direct reports).
Prefix: direct/.  URL names: capp_dir_*.  Included by Capp/urls.py."""
from django.urls import path

from Capp.direct.statutory import capp_dir_statutory

urlpatterns = [
    path('direct/statutory/', capp_dir_statutory, name='capp_dir_statutory'),
]
