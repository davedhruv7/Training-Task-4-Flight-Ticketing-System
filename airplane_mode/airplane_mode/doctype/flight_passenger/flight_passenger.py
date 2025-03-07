# Copyright (c) 2025, Dhruv  and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class FlightPassenger(WebsiteGenerator):
	def before_save(self):
		first_name = self.first_name
		last_name = self.last_name
		self.full_name = f"{first_name} {last_name}".strip()
