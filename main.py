import jinja2
import webapp2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

from google.appengine.api import users

from google.appengine.ext import ndb

def get_outfit(gender, formal, time, season):
    url="nothing"
    if gender == "male" and formal == "casual" and time == "night" and season == "summer":
        url = 'https://i.pinimg.com/originals/d9/8d/f1/d98df1f8d91d351136400bb03444a3c2.jpg'
    elif gender == "male" and formal == "casual" and time == "night" and season == "spring":
        url = 'https://www.gravetics.com/wp-content/uploads/2017/06/White-T-shirt-Ripped-Jeans-With-Sneakers.jpg'
    elif gender == "male" and formal == "casual" and time == "night" and season == "fall":
        url = 'https://i.pinimg.com/originals/b1/26/8b/b1268b3fb4bff80534e66d0bd092dff8.jpg'
    elif gender == "male" and formal == "casual" and time == "night" and season == "winter":
        url = 'https://i.pinimg.com/originals/b3/ed/8d/b3ed8def0759009d48bcdf70fda07c26.jpg'
    elif gender == "male" and formal == "casual" and time == "day" and season == "summer":
        url = 'https://cdn.shopify.com/s/files/1/0071/3637/8998/articles/mens-grey-t-shirt-denim-shorts-white-trainers_600x600_crop_center.jpg?v=1547039071'
    elif gender == "male" and formal == "casual" and time == "day" and season == "spring":
        url = 'https://c.static-nike.com/a/images/t_PDP_1280_v1/f_auto/w3yj391hlbia0x2wvcad/sportswear-tech-fleece-mens-joggers-gXTOoz1v.jpg'
    elif gender == "male" and formal == "casual" and time == "day" and season == "fall":
        url = 'https://i.pinimg.com/736x/6f/3f/77/6f3f7771f0c66ab96017da22e1eea520--mens-fashion-styles-male-fashion.jpg'
    elif gender == "male" and formal == "casual" and time == "day" and season == "winter":
        url = 'https://i.styleoholic.com/2017/12/With-gray-sweater-black-scarf-beige-beanie-jeans-and-brown-boots.jpg'
    elif gender == "male" and formal == "business-casual" and time == "night" and season == "summer":
        url = 'https://i.pinimg.com/originals/2c/c9/c5/2cc9c530168a5bc50c49b0355686c172.jpg'
    elif gender == "male" and formal == "business-casual" and time == "night" and season == "spring":
        url = 'https://i.pinimg.com/originals/0b/4d/96/0b4d967219c5eaaa13e3353daee59967.jpg'
    elif gender == "male" and formal == "business-casual" and time == "night" and season == "fall":
        url = 'https://i.pinimg.com/474x/5a/ca/cd/5acacddb5acbb6a80098d5dae9deba6f.jpg'
    elif gender == "male" and formal == "business-casual" and time == "night" and season == "winter":
        url = 'https://i.pinimg.com/736x/1b/80/32/1b80328594c528f3d1ffd985c4db78c1--black-vest-black-beanie.jpg'
    elif gender == "male" and formal == "business-casual" and time == "day" and season == "summer":
        url = 'https://i.pinimg.com/originals/5c/40/93/5c40930533f6e61c1748baac4db8ab9d.jpg'
    elif gender == "male" and formal == "business-casual" and time == "day" and season == "spring":
        url = 'https://i.pinimg.com/236x/4e/fa/d1/4efad1fa353ee0f6c7e023b73eb1e4ce--ralph-lauren-shorts-polo-ralph-lauren.jpg'
    elif gender == "male" and formal == "business-casual" and time == "day" and season == "fall":
        url = 'https://i.pinimg.com/originals/16/2f/26/162f262abe61d6c7c6ab73d59334cb13.jpg'
    elif gender == "male" and formal == "business-casual" and time == "day" and season == "winter":
        url = 'https://i.pinimg.com/originals/00/5a/2e/005a2e598a91a254b5c95e90cb8f8b8c.jpg'
    elif gender == "male" and formal == "fancy" and time == "night" and season == "summer":
        url = 'https://i.pinimg.com/originals/60/82/5e/60825ebd3c3c0af20ac3f81125d0f48f.jpg'
    elif gender == "male" and formal == "fancy" and time == "night" and season == "spring":
        url = 'https://i.pinimg.com/originals/ba/64/65/ba6465464d059c5dc1a1ddb5821cf2d6.jpg'
    elif gender == "male" and formal == "fancy" and time == "night" and season == "fall":
        url = 'https://i.pinimg.com/originals/9e/1d/34/9e1d341b4b6a6d6ddff0f939fafc5bb8.jpg'
    elif gender == "male" and formal == "fancy" and time == "night" and season == "winter":
        url = 'https://cdn.lookastic.com/looks/overcoat-double-breasted-blazer-crew-neck-t-shirt-large-32632.jpg'
    elif gender == "male" and formal == "fancy" and time == "day" and season == "summer":
        url = 'https://i.pinimg.com/736x/da/1c/47/da1c4767dc6202daad64be7aac9389bf.jpg'
    elif gender == "male" and formal == "fancy" and time == "day" and season == "spring":
        url = 'https://cdn.lookastic.com/looks/black-suit-beige-long-sleeve-shirt-black-low-top-sneakers-large-37539.jpg'
    elif gender == "male" and formal == "fancy" and time == "day" and season == "fall":
        url = 'https://i.pinimg.com/736x/b7/35/71/b7357108d4e5fe872c672695f4f263d0--fashion-for-men-fashion-styles.jpg'
    elif gender == "male" and formal == "fancy" and time == "day" and season == "winter":
        url = 'https://cdn.lookastic.com/looks/overcoat-blazer-long-sleeve-shirt-original-5859.jpg'
    elif gender == "female" and formal == "casual" and time == "night" and season == "summer":
        url = 'https://i.pinimg.com/originals/e2/36/b5/e236b5bcb07b180943f363f7f4866797.jpg'
    elif gender == "female" and formal == "casual" and time == "night" and season == "spring":
        url = 'https://i.pinimg.com/736x/a9/f1/45/a9f1454c8d78164c50fb14e4147e4994.jpg'
    elif gender == "female" and formal == "casual" and time == "night" and season == "fall":
        url = 'https://i.pinimg.com/originals/e3/0b/e1/e30be12d6e7f4800e8d4185106144af2.jpg'
    elif gender == "female" and formal == "casual" and time == "night" and season == "winter":
        url = 'https://i.pinimg.com/736x/6d/2a/eb/6d2aebf18e7c3d7af50d011eb7172580.jpg'
    elif gender == "female" and formal == "casual" and time == "day" and season == "summer":
        url = 'https://i.pinimg.com/originals/d7/de/b0/d7deb0e44c6535d3a5996dd8f5ec1f3f.jpg'
    elif gender == "female" and formal == "casual" and time == "day" and season == "spring":
        url = 'https://i.pinimg.com/originals/fa/f3/e0/faf3e09fc185762469cfdf7032f4cfb6.jpg'
    elif gender == "female" and formal == "casual" and time == "day" and season == "fall":
        url = 'https://i.pinimg.com/originals/b1/30/97/b1309763d29c3b20d903718b3e01122d.jpg'
    elif gender == "female" and formal == "casual" and time == "day" and season == "winter":
        url = 'https://i.pinimg.com/originals/aa/72/d8/aa72d82c73fbf44666fafc19c05a3add.jpg'
    elif gender == "female" and formal == "business-casual" and time == "night" and season == "summer":
        url = 'https://images.nyandcompany.com/is/image/NewYorkCompany/productlist2/Cold-Shoulder-Sheath-Dress_07722285_950.jpg'
    elif gender == "female" and formal == "business-casual" and time == "night" and season == "spring":
        url = 'https://mauricesprodatg.scene7.com/is/image/mauricesProdATG/112205_C2260?$large$'
    elif gender == "female" and formal == "business-casual" and time == "night" and season == "fall":
        url = 'https://i.pinimg.com/736x/f1/e1/43/f1e143acd67e4174b246cea7a921022f--fashion-makeup-photography-yellow-pants.jpg'
    elif gender == "female" and formal == "business-casual" and time == "night" and season == "winter":
        url = 'https://i.pinimg.com/originals/86/75/d5/8675d5766a3ac4af60aca03e10b1d25f.jpg'
    elif gender == "female" and formal == "business-casual" and time == "day" and season == "summer":
        url = 'https://media.missguided.com/s/missguided/DE929237_set/1/black-extreme-ruched-bandeau-bodycon-midi-dress'
    elif gender == "female" and formal == "business-casual" and time == "day" and season == "spring":
        url = 'https://i.pinimg.com/originals/15/0a/63/150a6309c38fd8402f269e230ec4e8cf.jpg'
    elif gender == "female" and formal == "business-casual" and time == "day" and season == "fall":
        url = 'https://i.pinimg.com/736x/af/79/b3/af79b32cb3607a6ca23723497410c8ec--stylish-spring-outfits-chic-work-outfit-spring.jpg'
    elif gender == "female" and formal == "business-casual" and time == "day" and season == "winter":
        url = 'https://i.pinimg.com/474x/ca/a8/20/caa8207fe4c2a59146558353928a9f09--business-casual-womens-fashion-winter-business-casual-clothes.jpg'
    elif gender == "female" and formal == "fancy" and time == "night" and season == "summer":
        url = 'https://i.pinimg.com/originals/ba/ec/c9/baecc9350e35af4dbdb1ae80c5bb5081.jpg'
    elif gender == "female" and formal == "fancy" and time == "night" and season == "spring":
        url = 'https://photo.venus.com/im/19017681.jpg?preset=pl-hero'
    elif gender == "female" and formal == "fancy" and time == "night" and season == "fall":
        url = 'https://i.pinimg.com/736x/07/6b/01/076b01b0dfc54388c2b64d26bbe9c044--luxury-dresses-luxury-outfits.jpg'
    elif gender == "female" and formal == "fancy" and time == "night" and season == "winter":
        url = 'https://i.pinimg.com/originals/82/14/7e/82147ec31ad1ee2c55853bea247050b9.jpg'
    elif gender == "female" and formal == "fancy" and time == "day" and season == "summer":
        url = 'https://i.pinimg.com/originals/29/a0/f9/29a0f9b0e003e42742e65df72ded5ae3.jpg'
    elif gender == "female" and formal == "fancy" and time == "day" and season == "spring":
        url = 'https://www.shopakira.com/media/catalog/product/cache/1/small_image/600x906.75/9df78eab33525d08d6e5fb8d27136e95/f/a/falling-in-love-off-the-shoulder-mini-dress_light-pink_1.jpg'
    elif gender == "female" and formal == "fancy" and time == "day" and season == "fall":
        url = 'https://i.pinimg.com/736x/70/e5/34/70e5346429ac7a2dfc64af1f10832def.jpg'
    elif gender == "female" and formal == "fancy" and time == "day" and season == "winter":
        url = 'https://i.pinimg.com/originals/f6/6f/03/f66f03710fd79638ba5280379f08f754.jpg'
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
            About = the_jinja_env.get_template('Templates/AboutUs.html')
            a_variable_dict = {"greeting": "Welcome to the Xcuslive Xperience!"}
            self.response.write(About.render(a_variable_dict))
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
        meme_img_choice = self.request.get('gender', 'formality', 'time', 'season' )

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
        Gender = self.request.get('gender')
        Formality = self.request.get('formality')
        Time = self.request.get('time')
        Season = self.request.get('season')
        print " "+Gender+" "+Formality+" "+Time+" "+Season
        # meme_img_choice = self.request.get('meme-type')
        url=get_outfit(Gender, Formality, Time, Season)
        pic_url = {"pic_url":url}

        self.response.write(results_template.render(pic_url))

class AboutMyFamilyHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('Templates/about_my_family.html')
        self.response.write(template.render())

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('Templates/new_post.html')
        self.response.write(template.render())
    def post(self):
        # Use the user input to create a new blog post
        title_input = self.request.get('title')
        content_input = self.request.get('content')
        name_input = self.request.get('name')

        blog_post = Post(title=title_input, content=content_input)
        blog_post.put()

        # Get the Author if one already exists with that name, or create one
        # otherwise. Add the new blog post to their list of posts.
        # Note: if you didn't create an Author Model, your `post` method will
        # look very different. See below for an alternative.
        check_authors = Author.query(Author.username == name_input).fetch()
        if len(check_authors) > 0:
            author = check_authors[0]
            author.posts.append(blog_post.key)
        else:
            author = Author(username=name_input, posts=[blog_post.key])

        author.put()

        # Create a list of all the blog post objects by the given author
        blog_posts = []
        for blog_post_key in author.posts:
            blog_posts.append(blog_post_key.get())

        # Render the template
        template_vars = {
            'username': name_input,
            'blog_posts': blog_posts
        }
        template = the_jinja_env.get_template(
            'Templates/show_posts.html')
        self.response.write(template.render(template_vars))

class Index(webapp2.RequestHandler):
    def get(self):
        index = the_jinja_env.get_template('Templates/index.html')
        self.response.write(index.render())


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/Xperience', Xperience),
    ('/AboutUs', AboutUs),
    ('/Recent', Recent),
    ('/Results', Results),
    ('/Welcome', WelcomePage),
    ('/family', AboutMyFamilyHandler),
    ('/posts', BlogHandler),
    ('/index', Index),

], debug=True)
