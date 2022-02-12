// Copyright (c) 2022, momscode and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sales report"] = {
	"filters": [
{
	"fieldname":"To date",
	"label": __("To date"),
	"fieldtype": "Date",

},
{
	"fieldname":"From date",
	"label": __("From date"),
	"fieldtype": "Date",
},
{
	"fieldname":"Customer",
	"label": __("Customer"),
	"fieldtype": "Link",
	"options":"Customer",
}
	

]
	


		
		
};
