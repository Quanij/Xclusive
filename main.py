import jinja2
import webapp2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

from google.appengine.api import users

from google.appengine.ext import ndb

def get_outfit(formal, time, season):
    url="nothing"
    if formal == "casual" and time == "night" and season == "summer":
        url = 'https://i.pinimg.com/originals/d9/8d/f1/d98df1f8d91d351136400bb03444a3c2.jpg'
    elif formal == "casual" and time == "night" and season == "spring":
        url = 'https://www.gravetics.com/wp-content/uploads/2017/06/White-T-shirt-Ripped-Jeans-With-Sneakers.jpg'
    elif formal == "casual" and time == "night" and season == "fall":
        url = 'https://i.pinimg.com/originals/b1/26/8b/b1268b3fb4bff80534e66d0bd092dff8.jpg'
    elif formal == "casual" and time == "night" and season == "winter":
        url = 'https://i.pinimg.com/originals/b3/ed/8d/b3ed8def0759009d48bcdf70fda07c26.jpg'
    elif formal == "casual" and time == "day" and season == "summer":
        url = 'https://cdn.shopify.com/s/files/1/0071/3637/8998/articles/mens-grey-t-shirt-denim-shorts-white-trainers_600x600_crop_center.jpg?v=1547039071'
    elif formal == "casual" and time == "day" and season == "spring":
        url = 'https://c.static-nike.com/a/images/t_PDP_1280_v1/f_auto/w3yj391hlbia0x2wvcad/sportswear-tech-fleece-mens-joggers-gXTOoz1v.jpg'
    elif formal == "casual" and time == "day" and season == "fall":
        url = 'https://i.pinimg.com/736x/6f/3f/77/6f3f7771f0c66ab96017da22e1eea520--mens-fashion-styles-male-fashion.jpg'
    elif formal == "casual" and time == "day" and season == "winter":
        url = 'https://i.styleoholic.com/2017/12/With-gray-sweater-black-scarf-beige-beanie-jeans-and-brown-boots.jpg'
    elif formal == "business-casual" and time == "night" and season == "summer":
        url = 'https://i.pinimg.com/originals/2c/c9/c5/2cc9c530168a5bc50c49b0355686c172.jpg'
    elif formal == "business-casual" and time == "night" and season == "spring":
        url = 'https://i.pinimg.com/originals/0b/4d/96/0b4d967219c5eaaa13e3353daee59967.jpg'
    elif formal == "business-casual" and time == "night" and season == "fall":
        url = 'https://i.pinimg.com/474x/5a/ca/cd/5acacddb5acbb6a80098d5dae9deba6f.jpg'
    elif formal == "business-casual" and time == "night" and season == "winter":
        url = 'https://i.pinimg.com/736x/1b/80/32/1b80328594c528f3d1ffd985c4db78c1--black-vest-black-beanie.jpg'
    elif formal == "business-casual" and time == "day" and season == "summer":
        url = 'https://i.pinimg.com/originals/5c/40/93/5c40930533f6e61c1748baac4db8ab9d.jpg'
    elif formal == "business-casual" and time == "day" and season == "spring":
        url = 'https://i.pinimg.com/236x/4e/fa/d1/4efad1fa353ee0f6c7e023b73eb1e4ce--ralph-lauren-shorts-polo-ralph-lauren.jpg'
    elif formal == "business-casual" and time == "day" and season == "fall":
        url = 'https://i.pinimg.com/originals/16/2f/26/162f262abe61d6c7c6ab73d59334cb13.jpg'
    elif formal == "business-casual" and time == "day" and season == "winter":
        url = 'https://i.pinimg.com/originals/00/5a/2e/005a2e598a91a254b5c95e90cb8f8b8c.jpg'
    elif formal == "fancy" and time == "night" and season == "summer":
        url = 'https://i.pinimg.com/originals/60/82/5e/60825ebd3c3c0af20ac3f81125d0f48f.jpg'
    elif formal == "fancy" and time == "night" and season == "spring":
        url = 'https://i.pinimg.com/originals/ba/64/65/ba6465464d059c5dc1a1ddb5821cf2d6.jpg'
    elif formal == "fancy" and time == "night" and season == "fall":
        url = 'https://i.pinimg.com/originals/9e/1d/34/9e1d341b4b6a6d6ddff0f939fafc5bb8.jpg'
    elif formal == "fancy" and time == "night" and season == "winter":
        url = 'https://cdn.lookastic.com/looks/overcoat-double-breasted-blazer-crew-neck-t-shirt-large-32632.jpg'
    elif formal == "fancy" and time == "day" and season == "summer":
        url = 'https://i.pinimg.com/736x/da/1c/47/da1c4767dc6202daad64be7aac9389bf.jpg'
    elif formal == "fancy" and time == "day" and season == "spring":
        url = 'https://cdn.lookastic.com/looks/black-suit-beige-long-sleeve-shirt-black-low-top-sneakers-large-37539.jpg'
    elif formal == "fancy" and time == "day" and season == "fall":
        url = 'https://i.pinimg.com/736x/b7/35/71/b7357108d4e5fe872c672695f4f263d0--fashion-for-men-fashion-styles.jpg'
    elif formal == "fancy" and time == "day" and season == "winter":
        url = 'https://cdn.lookastic.com/looks/overcoat-blazer-long-sleeve-shirt-original-5859.jpg'
    return url

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
        meme_img_choice = self.request.get('formality', 'time', 'season' )

        pic_url = get_outfit(meme_img_choice)

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
    def post(self):
        results = the_jinja_env.get_template('results.html')
        self.response.write(results.render())

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('Templates/welcome.html')
        a_variable_dict = {"greeting": "Welcome to the Xcuslive Xperience!"}
        self.response.write(welcome_template.render(a_variable_dict))

    def post(self):
        results_template = the_jinja_env.get_template('Templates/results.html')
        Formality = self.request.get('formality')
        Time = self.request.get('time')
        Season = self.request.get('season')
        print " "+Formality+" "+Time+" "+Season
        # meme_img_choice = self.request.get('meme-type')
        url=get_outfit(Formality, Time, Season)
        pic_url = {"pic_url":url}

        self.response.write(results_template.render(pic_url))


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/Xperience', Xperience),
    ('/AboutUs', AboutUs),
    ('/Recent', Recent),
    ('/Results', Results),
    ('/Welcome', WelcomePage),

], debug=True)
