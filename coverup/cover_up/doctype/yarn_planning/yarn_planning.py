import frappe
from frappe.utils import flt
from frappe.model.document import Document


class YarnPlanning(Document):
    pass


@frappe.whitelist()
def fetch_fabric_data_for_knitted(sales_order, knitted_planning):
    """
    FINAL IMPLEMENTATION

    For ONE Sales Order:
    - Fetch ALL submitted Fabric Planning docs
    - GROUP rows ONLY IF ALL are SAME:
        sub_finished_item_code,
        gsm,
        width
    - SUM:
        grand_total
        knit_waste
    - Calculate actual_required_total PER GROUP
    - Bind grouped rows into Knitted Planning child table
    """

    # --------------------------------------------------
    # 0️⃣ Validation
    # --------------------------------------------------
    if not sales_order:
        frappe.throw("Sales Order is required")

    if not knitted_planning:
        frappe.throw("Knitted Planning document is required")

    # --------------------------------------------------
    # 1️⃣ Fetch submitted Fabric Planning docs
    # --------------------------------------------------
    rows = frappe.get_all(
        "Yarn Planning",
        filters={
            "sales_order": sales_order,
            "docstatus": 1
        },
        fields=["name"]
    )

    yarn_plans = [
        frappe.get_doc("Yarn Planning", r.name)
        for r in rows if r.name
    ]

    if not yarn_plans:
        frappe.throw(
            f"No submitted Yarn Planning found for Sales Order {sales_order}"
        )

    # --------------------------------------------------
    # 2️⃣ GROUP & SUM TOTALS
    # --------------------------------------------------
    grouped = {}
    """
    grouped key =
        (
            sub_finished_item_code,
            gsm,
            width
        )

    grouped value =
        {
            sub_finished_item_code,
            gsm,
            width,
            grand_total,    <-- SUMMED
            knit_waste,     <-- SUMMED
            actual_required_total
        }
    """

    for fp in yarn_plans:

        sub_finished = (fp.sub_finished_item_code or "").strip()
        gsm = flt(fp.gsm or 0)
        width = flt(fp.width or 0)

        group_key = (
            sub_finished,
            gsm,
            width
        )

        if group_key not in grouped:
            # representative child row
            first_row = (fp.final_table or [None])[0]

            grouped[group_key] = {
                "sub_finished_item_code": sub_finished,
                "gsm": gsm,
                "width": width,
                "grand_total": 0.0,
                "knit_waste": 0.0,
                "item_code": first_row.item_code if first_row else None,
                "source_sub_code": first_row.description if first_row else None,
            }

        # ✅ SUM grand_total
        fp_grand_total = flt(fp.grand_total or 0)
        if not fp_grand_total:
            fp_grand_total = sum(
                flt(r.final_qty or 0) for r in (fp.final_table or [])
            )

        grouped[group_key]["grand_total"] += fp_grand_total

        # ✅ SUM knit_waste
        grouped[group_key]["knit_waste"] += flt(fp.knit_waste or 0)

    # --------------------------------------------------
    # 3️⃣ Calculate actual_required_total PER GROUP
    # --------------------------------------------------
    for data in grouped.values():
        data["actual_required_total"] = round(
            (100.0 - data["knit_waste"]) / 100.0 * data["grand_total"],
            6
        )

    # --------------------------------------------------
    # 4️⃣ Update Knitted Planning
    # --------------------------------------------------
    kp = frappe.get_doc("Knitted Planning", knitted_planning)
    kp.set("knitted_items", [])

    # Parent grand total = SUM of grouped grand totals
    kp.grand_total = sum(
        data["grand_total"] for data in grouped.values()
    )

    for data in grouped.values():
        kp.append("knitted_items", {
            "item_code": data["item_code"],
            "source_sub_code": data["source_sub_code"],
            "sub_finished_item_code": data["sub_finished_item_code"],
            "knitted_fabric": data["sub_finished_item_code"],
            "gsm": data["gsm"],
            "width": data["width"],
            "grand_total": data["grand_total"],
            "knit_waste": data["knit_waste"],              # ✅ SUMMED
            "qty": data["grand_total"],
            "actual_required_total": data["actual_required_total"]
        })

    kp.save(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "success",
        "sales_order": sales_order,
        "yarn_planning_count": len(yarn_plans),
        "groups_created": len(grouped),
        "knitted_grand_total": kp.grand_total
    }
