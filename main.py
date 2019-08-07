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
        if not user:
            signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
            email_adress = user.nickmame()
            cssi_user = CssiUser.query().filter(CssiUser().email == email_adress).get()
            if cssi_user:
                index = the_jinja_env.get_template('Templates/AboutUs.html')
                self.response.write(index.render())
            else:
                # Registration form for a first-time visitor:
                self.response.write('''
                Welcome to our site, %s!  Please sign up! <br>
                <form method="post" action="/">
                <input type="text" name="first_name">
                <input type="text" name="last_name">
                <input type="submit">
                </form><br> %s <br>
                ''' % (email_address, signout_link_html))

        else:
            login_url = users.create_login_url('/')
            index = the_jinja_env.get_template('Templates/LoginPage.html')
            templatedata ={"login_url":login_url}
            self.response.write(index.render(templatedata))


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
        welcome_template = the_jinja_env.get_template('Templates/welcome.html')
        a_variable_dict = {"greeting": "Welcome to the Xcuslive Xperience!"}
        self.response.write(welcome_template.render(a_variable_dict))


class Xperience(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('Templates/welcome.html')
        a_variable_dict = {"greeting": "Welcome to the Xcuslive Xperience!"}
        self.response.write(welcome_template.render(a_variable_dict))

    def post(self):
        results_template = the_jinja_env.get_template('Templates/results.html')
        meme_img_choice = self.request.get('meme-type')

        pic_url = get_meme_url(meme_img_choice)

        the_variable_dict = {"img_url": pic_url}
        self.response.write(results_template.render(the_variable_dict))

class AboutUs(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('Templates/AboutUs.html')
        self.response.write(welcome_template.render())



app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/Xperience', Xperience),
    ('/AboutUs', AboutUs),

], debug=True)
