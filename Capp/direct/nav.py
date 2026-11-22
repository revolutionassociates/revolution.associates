"""Navigation entries for the Capp menu (frozen contract, see docs/capp_upgrade/00_MASTER_PLAN.md section 5).

Each item: {"label", "url_name", "perm", "modes"}; modes subset of {"DIRECT","ASSOCIATE"}.
"""
NAV = [
    {"label": "Registers", "url_name": "capp_dir_registers",
     "perm": "payroll.process", "modes": ["DIRECT"]},
    {"label": "Statutory reports", "url_name": "capp_dir_reports",
     "perm": "challan.download", "modes": ["DIRECT"]},
    {"label": "Month-end checklist", "url_name": "capp_dir_checklist",
     "perm": "payroll.process", "modes": ["DIRECT"]},
    {"label": "Challans and returns", "url_name": "capp_dir_challans",
     "perm": "challan.download", "modes": ["DIRECT"]},
    {"label": "Payroll batches", "url_name": "capp_dir_payroll",
     "perm": "payroll.process", "modes": ["DIRECT"]},
    {"label": "Statutory setup", "url_name": "capp_dir_statutory",
     "perm": "statutory.edit", "modes": ["DIRECT"]},
]
