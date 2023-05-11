import os

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
            <link href="/static/css/style.css" rel="stylesheet">
          </head>
          <body>
            <p>Warna</p>
          </body>
        </html>"""

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.getcwd()
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'C:/Project/Project Programming/python/src/02 - Cherrypy/public'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)