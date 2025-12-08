import frappe
from frappe.utils import flt
from frappe import _





# @frappe.whitelist()
# def create_knitted_planning_from_fabric(fabric_docname):
#     """
#     Creates Knitted Planning from Fabric Planning.
#     Uses your Knitted Planning doctype fields exactly:
#     fabric_planning_ref, grand_total, waste_, actual_required, gsm, width, sales_order, knitted_items
#     """
#     # load source
#     doc = frappe.get_doc("Fabric Planning", fabric_docname)

#     # HEADER values (robust: try common alternatives)
#     grand_total = flt(doc.get("grand_total") or doc.get("Grand Total") or 0)
#     # NOTE: your KnittedPlanning uses fieldname 'waste_' so we read source waste percent from common names
#     waste_percent = flt(doc.get("waste_percent") or doc.get("knit_waste") or doc.get("waste") or doc.get("waste_") or 0)
#     header_gsm = doc.get("gsm") or doc.get("GSM") or None
#     header_width = doc.get("width") or doc.get("Width") or None
#     sales_order = doc.get("sales_order") or doc.get("sales_order_ref") or None

#     # calculate actual required based on waste%
#     actual_required_total = (100.0 - waste_percent) / 100.0 * grand_total

#     # detect first table-type child field for rows (robust)
#     child_rows = []
#     for f in doc.meta.get("fields"):
#         if f.get("fieldtype") == "Table":
#             candidate = doc.get(f.get("fieldname"))
#             if candidate:
#                 child_rows = candidate
#                 break

#     # fallback known child names (from your screenshot)
#     if not child_rows:
#         child_rows = doc.get("final_table") or doc.get("final table") or doc.get("fabric_items") or doc.get("final_table") or []

#     # gather per-row info
#     rows_info = []
#     total_absolute = 0.0
#     total_percentage = 0.0
#     has_percentage = False

#     for r in (child_rows or []):
#         # detect source sub finished code
#         sub_code = r.get("sub_finished_item_code") or r.get("sub_item_code") or r.get("item_code") or r.get("Item Code") or None

#         # absolute qty candidates
#         absolute = None
#         for key in ("final_quantity", "final_qty", "req_from_knitting", "required", "qty", "quantity", "amount"):
#             if r.get(key) not in (None, ""):
#                 absolute = flt(r.get(key))
#                 break

#         # percentage field
#         pct = flt(r.get("percentage") or r.get("percent") or 0)
#         if pct:
#             has_percentage = True
#             total_percentage += pct

#         rows_info.append({"row": r, "sub_code": sub_code, "absolute": absolute, "percentage": pct})
#         if absolute:
#             total_absolute += absolute

#     # allocate actual_required_total to rows
#     knitted_rows = []
#     if has_percentage and total_percentage > 0:
#         for info in rows_info:
#             qty = (info["percentage"] / total_percentage) * actual_required_total if info["percentage"] else 0.0
#             knitted_rows.append((info, qty))
#     elif total_absolute > 0:
#         scale = actual_required_total / total_absolute if total_absolute else 0.0
#         for info in rows_info:
#             absv = flt(info["absolute"] or 0)
#             qty = absv * scale
#             knitted_rows.append((info, qty))
#     else:
#         n = len(rows_info) or 1
#         per_row = actual_required_total / n
#         for info in rows_info:
#             knitted_rows.append((info, per_row))

#     # prepare Knitted Planning doc (use your exact doctype and fieldnames)
#     knit = frappe.new_doc("Knitted Planning")
#     knit.fabric_planning_ref = doc.name
#     knit.grand_total = grand_total
#     knit.waste_ = waste_percent      # note fieldname 'waste_'
#     knit.actual_required = flt(actual_required_total)
#     knit.gsm = header_gsm
#     knit.width = header_width
#     knit.sales_order = sales_order

#     # mapping function: sub -> knitted code (adjust if you have real mapping)
#     def map_to_knitted_code(sub_code):
#         if not sub_code:
#             return None
#         if sub_code.startswith("SF-"):
#             return sub_code.replace("SF-", "KN-")
#         if sub_code.startswith("SUB-"):
#             return sub_code.replace("SUB-", "KNIT-")
#         return "KN-" + str(sub_code)

#     # append child rows to knitted_items table
#     for (info, qty) in knitted_rows:
#         r = info["row"]
#         sub_code = info.get("sub_code")
#         knitted_code = map_to_knitted_code(sub_code)

#         row_gsm = r.get("gsm") or header_gsm
#         row_width = r.get("width") or header_width

#         knit.append("knitted_items", {
#             "item_code": knitted_code,
#             "source_sub_code": sub_code,
#             "qty": flt(qty),
#             "gsm": row_gsm,
#             "width": row_width,
#             "percentage": info.get("percentage") or 0.0
#         })

#     # insert (do not auto-submit unless you want)
#     knit.insert(ignore_permissions=True)

#     # optional message for UI; return name for API usage
#     frappe.msgprint(_("Knitted Planning created: {0}").format(knit.name))
#     return knit.name
