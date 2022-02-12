// Copyright (c) 2022, momscode and contributors
// For license information, please see license.txt

frappe.ui.form.on('customer1', {
	 /* refresh: function(frm){
		 frm.add_custom_button('Active',()=>{
			 frm.set_value('status','active')},'status')
		frm.add_custom_button('Inactive',()=>{
				 frm.set_value('status','inactive')
			 },'status')
			} */

			 refresh:function(frm){
				 frm.add_custom_button('Click',()=>{
					let c=frappe.db.count('customer1')
					frappe.msgprint("Total count is"+c) 
	

				})
				
			} 
			

			


	 
});
