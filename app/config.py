import os

WTF_CSRF_ENABLED = True

# set this environment variable and modify the name accordingly when deploying
SECRET_KEY = os.getenv('BASIC_FLASK_SECRET', 'you-will-never-guess')
