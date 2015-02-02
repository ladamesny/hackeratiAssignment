import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graph_data_hackerati.settings')

import django
django.setup()

from datetime import datetime
import requests
from graphchart.models import Reading
import kronos
import random

@kronos.register('*/5 * * * *')
def get_reading():
    url = 'https://polar-dawn-2893.herokuapp.com/'
    res = requests.get(url).json()
    Reading.objects.get_or_create(temperature=int(res['degrees']), reading_time=datetime.utcnow())
    pass
