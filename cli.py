import sys, datetime

'''
python cli.py [gen|anal] 
'''

if __name__=='__main__':
  calltime = datetime.datetime.now()

  if sys.argv[1] == 'gen':
    import form_generate
    name = input('Formname: ')
    formname = str(calltime).replace(':','_').replace('-','_').replace('.','_') + name
    n = int(input('Number of fields: '))
    fields = {}
    for _ in range(n):
      print(fields.keys())
      field = input('Field Name: ')
      while field in fields.keys(): field = input('field exists. Enter new name: ')
      length = int(input('Number of lines: '))
      fields[field] = length
    loc = form_generate.generate_form(formname,fields)
    print('Form created and saved at',loc)

  elif sys.argv[1] == 'anal':
    pass

  else:
    print('Please enter only \'gen\' or \'anal\' to generate a form or analyse a form respectively')
