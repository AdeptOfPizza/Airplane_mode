# Copyright (c) 2024, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneFlight(Document):
	def on_submit(self):
		self.status = 'Completed'
