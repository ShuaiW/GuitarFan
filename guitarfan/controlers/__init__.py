#!/usr/bin/env python
# -*- coding: utf-8 -*-

from admin.administrator import bp_admin_administrator
from admin.tab import bp_admin_tab
from error import bp_error

def Register_Blueprints(app):
    app.register_blueprint(bp_admin_administrator)
    app.register_blueprint(bp_admin_tab)
    app.register_blueprint(bp_error)