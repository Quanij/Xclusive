import jinja2
import webapp2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

from google.appengine.api import users

from google.appengine.ext import ndb



class CssiUser(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
# other functions should go above the handlers or in a separate file

class LoginPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
            email_adress = user.nickname()
            cssi_user = CssiUser.query().filter(CssiUser.email == email_adress).get()
            if cssi_user:
                About = the_jinja_env.get_template('Templates/AboutUs.html')
                a_variable_dict = {"greeting": "Welcome to the Xcuslive Xperience!"}
                self.response.write(About.render(a_variable_dict))
            else:
                # Registration form for a first-time visitor:
                self.response.write('''
                Welcome to our site, %s!  Please enter your name! <br><hr>
                <form method="post" action="/">
                <label for="first name"> First Name</label>
                <input type="text" name="first_name">
                <label for="Last name"> Last Name</label>
                <input type="text" name="last_name">
                <input type="submit">
                </form><br> %s <br>
                ''' % (email_adress, signout_link_html))

        else:
            login_url = users.create_login_url('/')
            template_login={"login_url":login_url}
            Login = the_jinja_env.get_template('Templates/LoginPage.html')
            self.response.write(Login.render(template_login))


    def post(self):
        user = users.get_current_user()
        # Create a new CSSI user.
        cssi_user = CssiUser(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name')
            )
        # Store that Entity in Datastore.
        cssi_user.put()
        # Show confirmation to the user. Include a link back to the index.
        #self.response.write('Thanks for signing up, %s! <br><a href="/Xperience">Home</a>' %cssi_user.first_name)
        About = the_jinja_env.get_template('Templates/AboutUs.html')
        a_variable_dict = {"greeting": "Welcome to the Xcuslive Xperience!"}
        self.response.write(About.render(a_variable_dict))


class Xperience(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('Templates/welcome.html')
        a_variable_dict = {"greeting": "Welcome to the Xcuslive Xperience!"}
        self.response.write(welcome_template.render(a_variable_dict))

    def post(self):
        results_template = the_jinja_env.get_template('Templates/results.html')
        meme_first_line = self.request.get('user-first-ln')
        meme_second_line = self.request.get('user-second-ln')
        meme_img_choice = self.request.get('meme-type')

        pic_url = get_meme_url(meme_img_choice)

        the_variable_dict = {"line1": meme_first_line,
                             "line2": meme_second_line,
                             "img_url": pic_url}
        self.response.write(results_template.render(the_variable_dict))

class AboutUs(webapp2.RequestHandler):
    def get(self):  # for a get request
        About = the_jinja_env.get_template('Templates/AboutUs.html')
        a_variable_dict = {"greeting": "Welcome to the Xcuslive Xperience!"}
        self.response.write(About.render(a_variable_dict))

class Recent(webapp2.RequestHandler):
    def get(self):
        Recent = the_jinja_env.get_template('Recent.html')
        self.response.write(Recent.render())

class Results(webapp2.RequestHandler):
    def get(self):
        results = the_jinja_env.get_template('results.html')
        self.response.write(results.render())


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/Xperience', Xperience),
    ('/AboutUs', AboutUs),
    ('/Recent', Recent),
    ('/Results', Results),

], debug=True)
