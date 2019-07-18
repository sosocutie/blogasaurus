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

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_env.get_template("templates/new_post.html")
        self.response.write(start_template.render())
    def post(self):
        title_var = self.request.get('post_title')
        post_var = self.request.get('post_content')
        author_var = self.request.get('author_name')

        post_vars = {
            "title_var": title_var,
            "post_var": post_var,
            "author_var": author_var,
            "date_and_time": "food",
            }
        template = jinja_env.get_template('templates/view_post.html')
        self.response.write(template.render(post_vars))

app = webapp2.WSGIApplication([
    ('/', blogasaurus),
    ('/make_post', BlogHandler)
], debug=True)
