import webapp2
from google.appengine.api import users
import jinja2
import os


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# other functions should go above the handlers or in a separate file
def get_meme_url(meme_choice):
    if meme_choice == 'casual':
        url = 'https://www.pacsun.com/dw/image/v2/AAJE_PRD/on/demandware.static/-/Sites-pacsun_storefront_catalog/default/dw39551ee1/product_images/0131103680006NEW_00_424.jpg?sw=690&sh=1070&sm=fit'
    elif meme_choice == 'business-casual':
        url = 'http://www.shorthairgirl.com/wp-content/uploads/2017/06/f6d7e__business-casual-swag-outfit.jpg'
    elif meme_choice == 'fancy':
        url = 'https://i.pinimg.com/736x/11/92/ef/1192efc1507690d552e2e6617d433b6c--casual-fridays-old-school.jpg'
    return url


class EnterInfoHandler(webapp2.RequestHandler):
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

    def get(self):
        user = users.get_current_user()
        if user:
          # The if block only runs if the user IS logged in.
          # The user has a method called `nickname()` that looks up their email.
          # We can use this information to show the user who they're logged in as.
          email_address = user.nickname()
          # Generate a sign out link - this does it all in one line.
          logout_link_html = '<a href="%s">sign out</a>' % (
                                users.create_logout_url('/'))
          # Show that sign out link on screen:
          self.response.write(
            "You're logged in as " + email_address + "<br>" + logout_link_html)
        else:
          # The else block only runs if the user isn't logged in.
          login_url = users.create_login_url('/')
          login_html_element = '<a href="%s">Sign in</a>' % login_url
          self.response.write('Please log in.<br>' + login_html_element)

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    # ('/memeresult', ShowMemeHandler)
], debug=True)
