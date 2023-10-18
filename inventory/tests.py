import sys 
sys.path.append('../')

from mysite.asgi import *
from inventory.models import Type

query = Type.objects.all()
print(query)

