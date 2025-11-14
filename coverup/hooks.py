app_name = "coverup"
app_title = "Cover Up"
app_publisher = "Sowaan"
app_description = "Purchase Order of Yarn Calculation Items"
app_email = "info@sowaan.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "coverup",
# 		"logo": "/assets/coverup/logo.png",
# 		"title": "Cover Up",
# 		"route": "/coverup",
# 		"has_permission": "coverup.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/coverup/css/coverup.css"
# app_include_js = "/assets/coverup/js/coverup.js"

# include js, css files in header of web template
# web_include_css = "/assets/coverup/css/coverup.css"
# web_include_js = "/assets/coverup/js/coverup.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "coverup/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}


# top-level of hooks.py
# doctype_js = {
#     "Yarn Calculation Sheet": "public/js/yarn_calculation_sheet.js"
# }



# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "coverup/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "coverup.utils.jinja_methods",
# 	"filters": "coverup.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "coverup.install.before_install"
# after_install = "coverup.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "coverup.uninstall.before_uninstall"
# after_uninstall = "coverup.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "coverup.utils.before_app_install"
# after_app_install = "coverup.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "coverup.utils.before_app_uninstall"
# after_app_uninstall = "coverup.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "coverup.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"coverup.tasks.all"
# 	],
# 	"daily": [
# 		"coverup.tasks.daily"
# 	],
# 	"hourly": [
# 		"coverup.tasks.hourly"
# 	],
# 	"weekly": [
# 		"coverup.tasks.weekly"
# 	],
# 	"monthly": [
# 		"coverup.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "coverup.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "coverup.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "coverup.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["coverup.utils.before_request"]
# after_request = ["coverup.utils.after_request"]

# Job Events
# ----------
# before_job = ["coverup.utils.before_job"]
# after_job = ["coverup.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"coverup.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

