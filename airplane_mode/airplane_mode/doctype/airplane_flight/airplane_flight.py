# Copyright (c) 2025, Dhruv  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class AirplaneFlight(Document):
    def autoname(self):
        """Generate a unique flight name in the format: Airplane-Code-MM-YYYY-00001"""
        if not self.airplane or not self.date_of_departure:
            frappe.throw("Airplane and Date of Departure are required for naming.")

        # Extract the Airplane Code (e.g., IndiGo-005)
        airplane_code = self.airplane

        # Convert date to MM-YYYY format
        flight_month_year = frappe.utils.formatdate(self.date_of_departure, "MM-yyyy")

        # Generate a 5-digit series number per airplane per month
        flight_series = make_autoname(f"{airplane_code}-{flight_month_year}-.#####")

        # Final name format
        self.name = flight_series