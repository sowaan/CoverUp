frappe.ui.form.on("Knitted Planning", {
    fabric_planning_ref(frm) {

        if (!frm.doc.fabric_planning_ref) return;

        // Auto-save if new
        if (frm.is_new()) {
            frm.save()
                .then(() => {
                    run_mapping(frm);
                })
                .catch(() => {
                    frappe.msgprint("Failed to save Knitted Planning.");
                });
            return;
        }

        // If already saved
        if (frm.doc.knitted_planning_item?.length) {
            frappe.confirm(
                __("Knitted Planning items already exist. Re-fetch?"),
                () => run_mapping(frm)
            );
        } else {
            run_mapping(frm);
        }
    }
});

function run_mapping(frm) {
    frappe.call({
        method: "coverup.cover_up.doctype.yarn_planning.yarn_planning.fetch_fabric_data_for_knitted",
        args: {
            sales_order: frm.doc.fabric_planning_ref,
            knitted_planning: frm.doc.name
        },
        freeze: true,
        callback(r) {
            if (r.message) {
                frappe.show_alert({
                    message: __("Fabric Planning loaded successfully"),
                    indicator: "green"
                });
                frm.reload_doc();
            }
        }
    });
}
