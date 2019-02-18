import form_generate

fields = {"Name": 1, "Roll no": 1, "Address": 4}
file_name = "test"
pos_file = open(file_name + ".txt", "w")

ans = form_generate.generate_form(file_name, fields)
pos_file.write(str(ans))
print(ans)