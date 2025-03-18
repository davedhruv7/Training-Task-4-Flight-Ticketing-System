// Copyright (c) 2025, Dhruv  and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Airline', {
//     refresh: function(frm) {
//         if (frm.doc.website) {
//             frm.add_custom_button('Visit Website', () => {
//                 window.open(frm.doc.website, '_blank');
//             }).addClass('btn btn-primary');
//         }
//     }
// });

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            frm.add_web_link(__(frm.doc.website), 'Visit Website');
        }
    }
});

// frappe.ui.form.on('Airline', {
//     refresh(frm) {
        // if (frm.doc.website) {
        //     frm.add_web_link(__(frm.doc.website), 'Visit Website');
        // }
// 	},
// });