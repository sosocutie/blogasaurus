import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class blogasaurus(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_env.get_template("templates/index.html")
        self.response.write(start_template.render())

app = webapp2.WSGIApplication([
    ('/', blogasaurus)
], debug=True)
