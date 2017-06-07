import os
import os.path
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'BookSummarySearch.settings'
import django
django.setup()

# imports for our project
from django.core import management
from django.db import connection
from Search import models
from scrapefunction.FourMin import FourMin
from scrapefunction.ReadItForMe import ReadItForMe
from scrapefunction.Blink import Blink
from scrapefunction.BizSum import SummaryService

def dropEverything():
  print('\nLiving on the edge!  Dropping the current database tables.')
  with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")
    migrations()

# make the migrations and migrate
def migrations():
  management.call_command('makemigrations')
  management.call_command('migrate')

def loadDataFromTxt(fh,model):
  print(' Working on this  ',model)
  file = open(fh,"r",encoding="utf-8")
  bookset = set()
  for line in file.readlines():
    name = ' '.join(line.split(',')[1:])
    url = line.split(',')[0]
    if name not in bookset:
      try:
        bookset.add(name)
        bookmodel = model()
        bookmodel.name = name.strip().lower()
        bookmodel.url = url.strip()
        bookmodel.save()
      except Exception as ex:
        print('K something went wrong.. Probably uniqueness ',ex)
        print('\nWe shall continue..')
        pass
     

# ensure the user really wants to do this
areyousure = input('''
  You can drop the entire db, or just make migrations. 
  Dropping will also apply the migrations.

  Please type 'yes' to confirm the data destruction, 'm' to only migrate: ''')
if areyousure.lower() == 'm':
  print()
  print('  Just making migrations and such..')
  migrations()

elif areyousure.lower() == 'yes':
  dropEverything()
else:
  loadDataFromTxt('BizSum.txt',models.BizSumMod) 
  loadDataFromTxt('Kirkus.txt',models.KirkusMod)
# FourMin.SummaryService()
# Blink.SummaryService()
# ReadItForMe.SummaryService()




