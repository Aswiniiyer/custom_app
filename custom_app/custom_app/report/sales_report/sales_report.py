# Copyright (c) 2022, momscode and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	conditions = ""

	if filters.get("from_date") and filters.get("to_date"):
		conditions += " and posting_date BETWEEN '{0}' and '{1}'".format(filters.get("from_date"),filters.get("to_date"))

	if filters.get("customer"):
		conditions += " and customer='{0}' ".format(filters.get("customer"))

	

	columns = [
		{"label": "Posting Date", "fieldname": "posting_date", "fieldtype": "Date", "width": "100"},
		{"label":"Payment Due Date","fieldname":"due_date","fieldtype":"Date","width":"100"},
	
	]
	query = """ SELECT * FROM `tabSales Invoice` WHERE docstatus=0 {0}""".format(conditions)
	data = frappe.db.sql(query, as_dict=1)

	return columns, data