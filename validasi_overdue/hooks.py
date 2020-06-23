# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "validasi_overdue"
app_title = "Validasi Overdue"
app_publisher = "DAS"
app_description = " "
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "helper.ptdas@gmail.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/validasi_overdue/css/validasi_overdue.css"
# app_include_js = "/assets/validasi_overdue/js/validasi_overdue.js"

# include js, css files in header of web template
# web_include_css = "/assets/validasi_overdue/css/validasi_overdue.css"
# web_include_js = "/assets/validasi_overdue/js/validasi_overdue.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "validasi_overdue.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "validasi_overdue.install.before_install"
# after_install = "validasi_overdue.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "validasi_overdue.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"validate": "validasi_overdue.custom_method.cek_invoice_overdue",
	},
	"Delivery Note": {
		"on_submit": "validasi_overdue.custom_method.copy_attachments",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"validasi_overdue.tasks.all"
# 	],
# 	"daily": [
# 		"validasi_overdue.tasks.daily"
# 	],
# 	"hourly": [
# 		"validasi_overdue.tasks.hourly"
# 	],
# 	"weekly": [
# 		"validasi_overdue.tasks.weekly"
# 	]
# 	"monthly": [
# 		"validasi_overdue.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "validasi_overdue.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "validasi_overdue.event.get_events"
# }

