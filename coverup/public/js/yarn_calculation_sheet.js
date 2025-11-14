// frappe.ui.form.on('Yarn Calculation Sheet', {
//     refresh(frm) {
//         console.log("✅ Yarn Calculation Sheet JS loaded from coverup app");
//     }
// });

// frappe.ui.form.on('Yarn Calculation Sheet', {
//     refresh: function(frm) {
//         if (!frm.doc.__islocal) {
//             frm.add_custom_button(__('Create Purchase Order'), function() {
//                 frappe.call({
//                     method: "coverup.cover_up.api.create_purchase_order.create_purchase_order_from_yarn",
//                     args: {
//                         yarn_docname: frm.doc.name
//                     },
//                     callback: function(r) {
//                         if(r.message){
//                             // Redirect to the newly created Purchase Order
//                             frappe.set_route("Form", "Purchase Order", r.message);
//                         }
//                     }
//                 });
//             });
//         }
//     }
// });
