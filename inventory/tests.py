import sys 
sys.path.append('../')

from mysite.asgi import *
from inventory.models import *

query = Category(name='Carpinteria')

query.save()

