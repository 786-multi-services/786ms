from setuptools import setup

import os

# Put here required packages
packages = [
	'Django>=1.10.3',
	'django-nocaptcha_recaptcha',
	'pillow',
	'django-786ms_career',
	'django-786ms_students',
	'django-786ms_shops'
]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='786ms',
      version='1.0',
      description='786 Multi Services',
      author='zeeshan',
      author_email='zkhan1093@example.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

