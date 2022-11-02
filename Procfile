release: sh -c 'python manage.py migrate && python manage.py loaddata initial_province_data.json && python manage.py loaddata initial_area_data.json'
web: gunicorn project_django.wsgi --log-file -