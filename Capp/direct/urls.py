"""URLs of the DIRECT track (statutory, challans, payroll processing, direct reports).
Prefix: direct/.  URL names: capp_dir_*.  Included by Capp/urls.py."""
from django.urls import path

from Capp.direct import payroll
from Capp.direct.statutory import capp_dir_statutory

urlpatterns = [
    path('direct/statutory/', capp_dir_statutory, name='capp_dir_statutory'),
    path('direct/payroll/', payroll.capp_dir_payroll, name='capp_dir_payroll'),
    path('direct/payroll/<int:pk>/', payroll.capp_dir_payroll_detail, name='capp_dir_payroll_detail'),
    path('direct/payroll/<int:pk>/process/', payroll.capp_dir_payroll_process, name='capp_dir_payroll_process'),
    path('direct/payroll/<int:pk>/reopen/', payroll.capp_dir_payroll_reopen, name='capp_dir_payroll_reopen'),
    path('direct/payroll/<int:pk>/finalize/', payroll.capp_dir_payroll_finalize, name='capp_dir_payroll_finalize'),
    path('direct/payroll/<int:pk>/paid/', payroll.capp_dir_payroll_paid, name='capp_dir_payroll_paid'),
    path('direct/payroll/<int:pk>/delete/', payroll.capp_dir_payroll_delete, name='capp_dir_payroll_delete'),
]
