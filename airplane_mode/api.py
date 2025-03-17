# import frappe # type: ignore

# @frappe.whitelist(allow_guest=True)
# def sign_up(email, full_name, password, role):
#     try:
#         # Check if the email already exists
#         if frappe.db.exists("User", email):
#             return {"message": "User already exists"}

#         # Create a new User document
#         user = frappe.get_doc({
#             "doctype": "User",
#             "email": email,
#             "first_name": full_name,
#             "new_password": password,
#             "send_welcome_email": 0,  # Prevent sending welcome email
#             "roles": [{"role": role}]  # Assign the selected role
#         })

#         user.insert(ignore_permissions=True)  # Ignore permissions for signup

#         frappe.db.commit()
#         return {"message": "success"}

#     except Exception as e:
#         frappe.log_error(f"Signup Error: {str(e)}", "Signup Failed")
#         return {"message": f"Error: {str(e)}"}
