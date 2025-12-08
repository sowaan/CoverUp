frappe.ui.form.on("Knitted Planning", {
    fabric_planning_ref: function(frm) {
        const fp = frm.doc.fabric_planning_ref;
        if (!fp) return;

        // if knitted_items already filled, ask user
        if (frm.doc.knitted_items && frm.doc.knitted_items.length) {
            frappe.confirm(
                "There are already rows in Knitted Items. Replace with values from selected Fabric Planning?",
                function() {
                    _fetch_and_populate(frm, fp);
                },
                function() {
                    // cancelled
                }
            );
        } else {
            _fetch_and_populate(frm, fp);
        }
    }
});

function _fetch_and_populate(frm, fabric_docname) {
    frappe.call({
        method: "coverup.cover_up.doctype.knitted_planning.knitted_planning.fetch_fabric_data_for_knitted",
        args: { fabric_docname: fabric_docname },
        callback: function(r) {
            if (!r.message) {
                frappe.msgprint("No data returned from Fabric Planning.");
                return;
            }
            const data = r.message;

            // set headers
            frm.set_value("grand_total", data.grand_total);
            // your fieldname is 'waste_' in Knitted Planning JSON — try both
            if (frm.fields_dict && frm.fields_dict.waste_) {
                frm.set_value("waste_", data.waste_percent);
            } else {
                frm.set_value("waste_percent", data.waste_percent);
            }
            // frm.set_value("actual_required", data.actual_required);
            // frm.set_value("gsm", data.gsm);
            // frm.set_value("width", data.width);
            frm.set_value("sales_order", data.sales_order);

            // clear existing child rows and populate knitted_items
            frm.clear_table("knitted_items");
            (data.rows || []).forEach(function(rw) {
                const row = frm.add_child("knitted_items");
                row.item_code = rw.item_code;
                row.source_sub_code = rw.description;
                row.qty = rw.qty;
                row.gsm = rw.gsm;
                row.width = rw.width;
                row.percentage = rw.percentage;
            });
            frm.refresh_field("knitted_items");
            frm.refresh_fields();
            frappe.msgprint("Knitted Planning populated from Fabric Planning: " + fabric_docname);
        }
    });
}
