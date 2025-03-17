import frappe

def send_rent_reminder():
    # settings = frappe.get_single("Rent Settings")
    
    # if not settings.enable_reminders:
    #     frappe.log_error("Rent reminders are disabled.", "Rent Reminder")
    #     return
    
    tenants = frappe.get_all("Rent Payment", 
        filters={"status": "Pending"}, 
        fields=["tenant", "rent_amount", "shop"]
    )
    
    for tenant in tenants:
        email = frappe.get_doc("Tenant",tenant.get('tenant')).email
        subject = f"Rent Reminder for {tenant.get('shop')}"
        message = f"""
        Dear {tenant.get('tenant')},

        This is a friendly reminder that your rent of {tenant.get('rent_amount')} is due for {tenant.get('shop')}.

        Please ensure payment is made on time.

        Regards,  
        Airport Management
        """
        
        
        frappe.sendmail(recipients=email, subject=subject, message=message)
        frappe.msgprint(f"Rent reminder sent to {tenant.get('tenant')}")
    frappe.db.commit()