import form_generate

fields = {"Name : ": 1, "Roll no : ": 1, "Address : ": 4}
file_name = "test"

ans = form_generate.generate_form(file_name, fields)
print(ans)