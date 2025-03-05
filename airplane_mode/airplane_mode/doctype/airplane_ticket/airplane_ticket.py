# Copyright (c) 2025, Dhruv and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

def prevent_submission(doc, method):
    """Prevent submission if status is not 'Boarded'."""
    if doc.status != "Boarded":
        frappe.throw(f"Submission failed! The current status is '{doc.status}'. Please update it to 'Boarded' before submitting.", title="Submission Error")


class AirplaneTicket(Document):
    def validate(self):
        """Called before saving the document."""
        self.remove_duplicate_addons()  # Ensure unique add-ons
        self.calculate_total_amount()  # Update total amount

    def remove_duplicate_addons(self):
        """Ensure each add-on type appears only once in the child table."""
        if not self.add_ons:  # Check if add-ons exist
            return  

        unique_addons = {}  # Dictionary to track added add-ons
        filtered_addons = []  # List to store unique add-ons

        for addon in self.add_ons:
            if addon.item not in unique_addons:  # Use 'item' instead of 'add_on_type'
                unique_addons[addon.item] = True  # Mark this add-on type as added
                filtered_addons.append(addon)  # Keep this add-on

        self.add_ons = filtered_addons  # Update the child table with only unique add-ons

    def calculate_total_amount(self):
        """Calculate Total Amount = Flight Price + Sum of add-ons."""
        self.total_amount = self.flight_price + sum(addon.amount for addon in self.add_ons)


    def before_insert(self):
        self.assign_seat()

    def assign_seat(self):
        """Assigns the next available seat for the flight."""
        booked_seats = frappe.get_all(
            "Airplane Ticket",
            filters={"flight": self.flight},
            fields=["seat"]
        )
        
        # Get a list of taken seats
        taken_seats = {ticket["seat"] for ticket in booked_seats if ticket["seat"]}

        # Possible seat numbers (e.g., A1, B2, etc.)
        all_seats = [f"{row}{col}" for row in "ABCDEF" for col in range(1, 31)]

        # Find the first available seat
        for seat in all_seats:
            if seat not in taken_seats:
                self.seat = seat
                return

        frappe.throw("No available seats for this flight!")
