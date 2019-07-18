import webapp2
import jinja2
import os
import datetime

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class FamilyPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/family.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/new_post.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

    def post(self):
        title_answer = self.request.get("title")
        content_answer = self.request.get("post-content")
        author_answer = self.request.get("author-name")

        template_vars = {
        "date_and_time": datetime.datetime.now().strftime("%B %d, %Y    %I:%M%p"),
        "title_answer":title_answer,
        "content_answer":content_answer,
        "author_answer":author_answer,
        }
        template = jinja_env.get_template('templates/view_post.html')
        self.response.write(template.render(template_vars))



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/family', FamilyPage),
    ('/blog', BlogHandler)
], debug=True)
