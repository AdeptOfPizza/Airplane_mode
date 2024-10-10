# Copyright (c) 2024, me and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document

class AirplaneTicket(Document):
	def validate(self):
		seen_items = []
		unique_add_ons = []
		unique_add_ons_cost = 0

		for addon in self.get("add_ons"):
			if addon.item not in seen_items:
				seen_items.append(addon.item)
				unique_add_ons.append(addon)
				unique_add_ons_cost += addon.amount

		self.set("add_ons", unique_add_ons)
		self.total_amount = self.flight_price + unique_add_ons_cost
        
	def before_submit(self):
		if not self.status == "Booked":
			frappe.throw('flight is not booked!')

	def before_insert(self):
		random_number = random.randint(1,99)

		letters = ('A', 'B', 'C', 'D', 'E')
		random_letter = random.choice(letters)

		self.seat = f'{random_number:02d}{random_letter}'