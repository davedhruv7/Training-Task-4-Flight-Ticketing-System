// Copyright (c) 2025, Dhruv  and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Flight", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airplane Flight', {
    source_airport: function(frm) {
        frm.set_query("destination_airport", function() {
            return {
                filters: [
                    ["name", "!=", frm.doc.source_airport] // Hide selected source airport from destination list
                ]
            };
        });
    },

    destination_airport: function(frm) {
        frm.set_query("source_airport", function() {
            return {
                filters: [
                    ["name", "!=", frm.doc.destination_airport] // Hide selected destination airport from source list
                ]
            };
        });
    }
});
