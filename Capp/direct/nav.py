"""Navigation entries for the Capp menu (frozen contract, see docs/capp_upgrade/00_MASTER_PLAN.md section 5).

Each item: {"label", "url_name", "perm", "modes"}; modes subset of {"DIRECT","ASSOCIATE"}.
"""
NAV = [
    {"label": "Statutory setup", "url_name": "capp_dir_statutory",
     "perm": "statutory.edit", "modes": ["DIRECT"]},
]
