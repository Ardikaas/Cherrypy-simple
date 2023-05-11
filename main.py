import os
import random
import string
import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('C:/Project/Project Programming/python/src/02 - Cherrypy/index.html')

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

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