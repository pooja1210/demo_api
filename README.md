# demo_api
### Getting Started

#### Requirements
- Python 3.6 & up
- Django version 3.1.1
-Django Rest Framework

Installation command
- pip install django
- pip install djangorestframework

Descritpion:-
Django Demo api is designed to speed up the performance of Django Rest Framework by using the cache as well as by query optimisation.
Here Cache used are Database based Cache and Memory based Cache.
#1 To use Database Cache:-
uncomment the Following Command from setting.Py

CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
      'LOCATION': 'my_table_name',
   }
}
and run the command
python manage.py createcachetable

This will create the tabe in Database named " demo-cache"

#2 To use Memory Based Cache
uncomment the Following Command from setting.py
Install memcached:
pip install python-memcached

CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
      'LOCATION': '127.0.0.1:11211',
   }
}
