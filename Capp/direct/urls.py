"""URLs of the DIRECT track (statutory, challans, payroll processing, direct reports).
Prefix: direct/.  URL names: capp_dir_*.  Included by Capp/urls.py."""
from django.urls import path

from Capp.direct import challans, checklist, payroll, registers, reports
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
    path('direct/challans/', challans.capp_dir_challans, name='capp_dir_challans'),
    path('direct/challans/ecr/create/', challans.capp_dir_ecr_create, name='capp_dir_ecr_create'),
    path('direct/challans/<int:year>/<int:month>/ecr/', challans.capp_dir_ecr_text, name='capp_dir_ecr_text'),
    path('direct/challans/<int:year>/<int:month>/epf-challan/', challans.capp_dir_epf_challan, name='capp_dir_epf_challan'),
    path('direct/challans/<int:year>/<int:month>/esi-challan/', challans.capp_dir_esi_challan, name='capp_dir_esi_challan'),
    path('direct/challans/<int:year>/<int:month>/esi-upload/', challans.capp_dir_esi_upload, name='capp_dir_esi_upload'),
    path('direct/challans/<int:year>/<int:month>/pt/', challans.capp_dir_pt_schedule, name='capp_dir_pt_schedule'),
    path('direct/challans/lwf/create/', challans.capp_dir_lwf_create, name='capp_dir_lwf_create'),
    path('direct/challans/lwf/<int:lwf_id>/challan/', challans.capp_dir_lwf_challan, name='capp_dir_lwf_challan'),
    path('direct/checklist/', checklist.capp_dir_checklist, name='capp_dir_checklist'),
    path('direct/reports/', reports.capp_dir_reports, name='capp_dir_reports'),
    path('direct/reports/<int:year>/<int:month>/<slug:kind>/', reports.capp_dir_report, name='capp_dir_report'),
    path('direct/reports/form24q/<str:financial_year>/', reports.capp_dir_form24q, name='capp_dir_form24q'),
    path('direct/registers/', registers.capp_dir_registers, name='capp_dir_registers'),
    path('direct/registers/<slug:key>/', registers.capp_dir_reg_list, name='capp_dir_reg_list'),
    path('direct/registers/<slug:key>/add/', registers.capp_dir_reg_add, name='capp_dir_reg_add'),
    path('direct/registers/<slug:key>/<int:pk>/delete/', registers.capp_dir_reg_delete, name='capp_dir_reg_delete'),
    path('direct/registers/<slug:key>/<int:year>/<int:month>/pdf/', registers.capp_dir_reg_download, name='capp_dir_reg_download'),
]
