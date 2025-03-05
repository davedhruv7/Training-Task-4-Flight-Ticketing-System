# Copyright (c) 2025, Dhruv  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document




class Airplane(Document):
    def autoname(self):
        # frappe.msgprint("Autoname function triggered!")
        
        if self.airline:
            airline_name = self.airline.replace(" ", "")

            count = frappe.db.count("Airplane", {"airline": self.airline}) + 1
            
            serial_number = f"{count:03d}"

            self.name = f"{airline_name}-{serial_number}"

            # frappe.msgprint(f"Generated Name: {self.name}")  
