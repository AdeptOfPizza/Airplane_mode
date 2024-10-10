# Copyright (c) 2024, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		self.full_name = self.first_name + ' ' + self.last_name

	def before_validate(self):
		seen_items = []
		unique_add_ons = []
		unique_add_ons_cost = 0

    
		for addon in self.add_ons:
			if addon.item not in seen_items:
            
				seen_items.append(addon.item)
				unique_add_ons.append(addon)
				unique_add_ons_cost += addon.amount

		self.add_ons = unique_add_ons

		self.total_amount = self.flight_price + unique_add_ons_cost

		

