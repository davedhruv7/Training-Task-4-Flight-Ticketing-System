# Copyright (c) 2025, Dhruv and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data()

    # Calculate total revenue
    total_revenue = sum(d["revenue"] for d in data)

    report_summary = [
        {"label": _("Total Revenue"), "value": total_revenue, "indicator": "Green"}
    ]

    # Chart Configuration
    chart = {
        "data": {
            "labels": [d["airline"] for d in data],
            "datasets": [{"values": [d["revenue"] for d in data]}],
        },
        "type": "donut",
    }

    return columns, data, None, chart, report_summary

def get_columns():
    """Define report columns."""
    return [
        {"label": _("Airline"), "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"label": _("Revenue"), "fieldname": "revenue", "fieldtype": "Currency", "width": 150},
    ]

def get_data():
    """Fetch revenue data grouped by airline."""
    airlines = frappe.get_all("Airline", fields=["name"])
    data = []

    for airline in airlines:
        revenue = frappe.db.sql("""
            SELECT SUM(at.total_amount) 
            FROM `tabAirplane Ticket` at
            JOIN `tabAirplane Flight` af ON at.flight = af.name
            JOIN `tabAirplane` a ON af.airplane = a.name
            WHERE a.airline = %s
        """, (airline.name,), as_list=True)[0][0] or 0

        data.append({"airline": airline.name, "revenue": revenue})

    return data