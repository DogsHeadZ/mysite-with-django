#-*- coding:utf-8 -*-
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'testfff.settings'

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    body_str = """
    <html>
        <head>
            <meta charset="utf-8">
            <title>DogsHead</title>
        </head>
        <body>
            <h1>mydearsite</h1>
            
        </body>
    </html>
    """
    body=[body_str]
    return body

from django.core.wsgi import get_wsgi_application
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(get_wsgi_application())
