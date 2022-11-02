release: sh -c 'python manage.py migrate && python manage.py loaddata initial_province_data.json && python manage.py loaddata initial_area_data.json && python manage.py loaddata initial_food.json && python manage.py loaddata initial_event.json && python manage.py loaddata data_faq.json'
web: gunicorn project_django.wsgi --log-file -
