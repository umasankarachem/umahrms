import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def execute():
	make_property_setter(
		"Purchase Order",
		"cost_center",
		"reqd",
		1,
		"Check",
		validate_fields_for_doctype=False,
	)
	frappe.clear_cache(doctype="Purchase Order")
