# a module is a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including django) as well as custom modules.

#core modules
import datetime
from datetime import date
import time
from time import time


#pip module
import camelcase
from camelcase import CamelCase

#import custom module
import custommodule
from custommodule import validate_email

#today = datetime.date.today()

#today = date.today()

timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))

email = 'test@test.com'
if validate_email(email):
    print('email is valid')
else:
    print('email is bad')
