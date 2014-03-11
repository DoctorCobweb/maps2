import jinja2
import webapp2
import os
import json

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



### request handlers ###
class MainPage (webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('templates/index.html')
	self.response.write(template.render())


### create the WSGI Application ###
routes = [
    ('/', MainPage)
]

app = webapp2.WSGIApplication(routes=routes, debug=True)
