// Copyright (c) 2025, Dhruv  and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
       
            frm.add_custom_button(__('Assign Seat'), function() {
                frappe.prompt([
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ], (values) => {
                    frm.set_value('seat', values.seat_number);
                    frm.save();
                }, __('Assign Seat'), __('Set'));
            });
        
    }
});
