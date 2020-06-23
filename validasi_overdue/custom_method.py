from __future__ import unicode_literals
import frappe
from frappe import _, msgprint, throw


@frappe.whitelist()
def cek_invoice_overdue(doc, method):
	invoice = frappe.db.sql(""" SELECT sinv.`name` FROM `tabSales Invoice` sinv
		WHERE sinv.`status` = "Overdue"
		AND sinv.`customer` = "{0}" """.format(doc.customer), as_dict = 1)

	if invoice :
		frappe.throw(_("Customer {0} masih memiliki invoice overdue").format(doc.customer))


@frappe.whitelist()
def copy_attachments(doc,method):

	sales_order = frappe.db.sql(""" SELECT DISTINCT(dni.`against_sales_order`) AS `sales_order` FROM `tabDelivery Note Item` dni WHERE dni.`parent` = "{}"
		""".format(doc.name), as_dict = 1)
	
	for s in sales_order:

		data =  frappe.db.sql(""" SELECT * FROM `tabFile` a WHERE a.`attached_to_doctype` = "Sales Order" AND a.`attached_to_name` = "{}" """.format(s.sales_order), as_dict = 1 )

		for d in data:
			file_so = frappe.get_doc('File', d.name)
			new_doc = frappe.new_doc('File')
			new_doc = file_so
			new_doc.attached_to_doctype = "Delivery Note"
			new_doc.attached_to_name = doc.name
			new_doc.insert()
	  