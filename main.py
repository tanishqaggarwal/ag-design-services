import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), 
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

class Index(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(JINJA_ENVIRONMENT.get_template("index.html").render())

class Portfolio(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(JINJA_ENVIRONMENT.get_template("portfolio.html").render())

app = webapp2.WSGIApplication([
  ('/', Index),
  ('/portfolio', Portfolio),], debug = True)