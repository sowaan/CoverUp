from frappe.model.document import Document
import frappe
from frappe.utils import flt
from frappe import _

class KnittedPlanning(Document): 
     pass
@frappe.whitelist()
def fetch_fabric_data_for_knitted(fabric_docname):
    """
    Fetch Fabric Planning header + final_table rows and return data for populating Knitted Planning.
    - Uses knit_waste field (exact) to compute:
        actual_required_total = (100 - knit_waste)/100 * grand_total
    - Maps final_table rows to knitted_items rows:
        item_code, description, qty (set to actual_required_total)
    """
    if not fabric_docname:
        frappe.throw(_("fabric_docname required"))

    # Load Fabric Planning
    doc = frappe.get_doc("Fabric Planning", fabric_docname)

    # Header values
    grand_total = flt(doc.get("grand_total") or 0)
    knit_waste = flt(doc.get("knit_waste") or 0)   # exact field name
    header_gsm = doc.get("gsm")
    header_width = doc.get("width")
    sales_order = doc.get("sales_order") or doc.get("sales_order_ref") or None

    # CORRECT FORMULA
    actual_required_total = (100.0 - knit_waste)/100 * grand_total
    actual_required_total = round(flt(actual_required_total), 6)  # keep precision (adjust decimals if needed)

    # Read the specific child table 'final_table'
    child_rows = doc.get("final_table") or []

    rows_out = []
    for r in (child_rows or []):
        item_code = r.get("item_code") 
        description = r.get("description")
        # (optional) you can use r.get("stitch_length") or r.get("percentage") if needed
        rows_out.append({
            "item_code": item_code,
            "description": description,
            # qty for each knitted row should show the SAME actual_required_total
            "qty": actual_required_total,
            "gsm":  header_gsm,
            "width":  header_width
            
        })

    return {
        "grand_total": grand_total,
        "waste_percent": knit_waste,
        "actual_required": actual_required_total,
        "gsm": header_gsm,
        "width": header_width,
        "sales_order": sales_order,
        "rows": rows_out
    }
