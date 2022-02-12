# Copyright (c) 2022, momscode and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class customer1(Document):
	def before_submit(self):
		exists=frappe.db.exists("customer1",
		{
			"customer1":self.customer1,
		},
		)
		if exists:
			frappe.throw("DB is existing")
