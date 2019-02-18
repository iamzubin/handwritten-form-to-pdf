import sys, datetime, os

from PIL import Image

'''
python cli.py [gen|anal]
'''

if __name__=='__main__':
  calltime = datetime.datetime.now()

  if sys.argv[1] == 'gen':
    import form_generate
    name = input('Formname: ')
    formname = name + '_' + str(calltime).replace(':','_').replace('-','_').replace('.','_')
    n = int(input('Number of fields: '))
    for _ in range(n):
      print(fields.keys())
      field = input('Field Name: ')
      while field in fields.keys(): field = input('field exists. Enter new name: ')
      length = int(input('Number of lines: '))
      fields[field] = length
    loc = form_generate.generate_form(formname,fields)
    print('Form created and saved at',loc)

  elif sys.argv[1] == 'anal':
    DATA = {}
    print('Sorry but code broke')
    print('See results from our test file below\n')
    demo_fields = {
      "name" : (100, 403, 2380, 547),
      "roll" :  (100, 553, 2380, 697),
      "address" : (100, 703, 2380, 1297)
    }
    import data_prep,vision
    if not os.path.isdir('tmp'): os.mkdir('tmp')
    field_files = data_prep.data_prep('test.png',demo_fields)
    for filename in field_files:
      text = vision.detect_document(filename)
      DATA[filename] = text
    for key in DATA.keys():
      field = key[key.find('/')+1:key.find('.png')]
      text = DATA[key]
      print(field,':',text)

  else:
    print('Please enter only \'gen\' or \'anal\' to generate a form or analyse a form respectively')
