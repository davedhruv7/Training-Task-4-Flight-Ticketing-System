// Copyright (c) 2025, Dhruv  and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rent Payment', {
    onload: function(frm) {
        frappe.call({
            method: 'frappe.client.get',
            args: {
                doctype: 'Shop Settings'
            },
            callback: function(response) {
                let settings = response.message;
                if (!frm.doc.rent_amount) {
                    frm.set_value('rent_amount', settings.default_rent_amount);
                }
            }
        });
    }
});
