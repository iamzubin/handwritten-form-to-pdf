#functions 

## data_prep.py -> data_prep

- input :  file (image), file ( dict { id : ( a,b,x,y  in sequence of crop function)  })

## form_generate.py -> generate_form

- input : (file name to generate), dict{ field_name: number of lines}
- eg : generate_form("test", {"Name :": 1, "Age :": 1, "Sex :": 1, "Email :": 1, "Home Address :": 4})