# in docker call gunicorn -b 0.0.0.0:9999 wsgi:application
import os
import sys

try:
    sys.path.append(r'usr/test_deploy/')
except:
    print('Failed to add path!')

from app import get_app

application = get_app()
if __name__ == '__main__':
    application.run(port=8888)
