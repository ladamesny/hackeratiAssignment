import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graph_data_hackerati.settings')

import django
django.setup()

from datetime import datetime
import requests
from graphchart.models import Reading

url = 'https://polar-dawn-2893.herokuapp.com/'

if __name__ == '__main__':
    res = requests.get(url).json()
    Reading.objects.get_or_create(temperature=int(res['degrees']), reading_time=datetime.utcnow())