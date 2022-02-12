# Copyright (c) 2022, momscode and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class shopee(Document):
	def validate(self):
		c=frappe.db.count('Store1')
		frappe.msgprint("Total count is {}".format(c))

	
	
