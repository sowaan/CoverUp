import frappe

@frappe.whitelist()
def create_purchase_order(yarn_docname):
    """
    Prepares an unsaved Purchase Order from a Yarn Calculation Sheet
    without automatic UOM conversion, and links it back to the Yarn Sheet.
    """
    # Load Yarn Calculation Sheet
    yarn_doc = frappe.get_doc("Yarn Calculation Sheet", yarn_docname)

    if not yarn_doc.yarn_requirement:
        frappe.throw("No items found in Yarn Requirement to create Purchase Order")

    po_items = []

    for row in yarn_doc.yarn_requirement:
        final_qty = getattr(row, "final_qty", 0)
        if not row.item_code or not final_qty:
            continue

        # Fetch UOM (ensure this field exists in child table)
        uom = getattr(row, "uom", None)

        # Append each item exactly as-is
        po_items.append({
            "item_code": row.item_code,
            "qty": final_qty,
            "uom": uom,
            "rate": getattr(row, "rate", 0),
            "schedule_date": frappe.utils.nowdate(),
        })

    if not po_items:
        frappe.throw("No valid items to include in Purchase Order")

    #frappe.msgprint(f"Yarn Doc: {yarn_docname}")
    # Prepare a new unsaved Purchase Order
    purchase_order_data = {
        "doctype": "Purchase Order",
        "custom_yarn_reference": yarn_docname,   # ✅ Reference field
        "custom_sales_order_reference": getattr(yarn_doc, "sales_order", None),  # Sales Order
        "items": po_items
    }

    return purchase_order_data
