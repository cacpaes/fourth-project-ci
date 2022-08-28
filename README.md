<h1>Taste Coffee</h1>
<p>Are you a coffee lover?<br>
Would you like to know what people are saying about a coffee you're looking forward to buying?<br>
This app is for you!<br>
On Taste Coffee, you can add your favorite coffees and comment on coffees already posted!<br>
Check it out!!
</P>

[View website in Heroku Pages](https://tastecoffee.herokuapp.com/)

![Picture4](https://user-images.githubusercontent.com/93129370/187056525-b34436f1-e3f1-4196-8d2d-d5040a8c04c3.png)


<h2>Contents</h2>
<h2>UX/UI Design</h2>
<h3>Strategy</h3>

<h3>Site goals</h3>

*  Create a platform that allows people (users) to post their favorite coffee and share their thoughts in comments on other posts.
*  The website is designed to be intuitive and easy to navigate.
*  The website was designed to be responsive and to meet all screen sizes.
*  The website should prioritize the display of the posts and present the content in a good way.


<h3>Agile</h3>

<p>For the development of this project, the Agile methodology was applied. As a support tool, I used the GitHub projects.</p>

[Go to this link for the project](https://github.com/users/cacpaes/projects/2/views/1)

<p>As you can see, we used a simple Kanban board with the fields (To do, Doing, Done). To do the next ones that will be executed, Doing the ones that are currently being developed and Done the ones that were finished.</p>


<h3>User stories</h3>

*  As a user, I want to understand the content of the website, so I can know if it's of my interest.
*  As a user, I want to easily navigate the site, so I can load the page with the content I want to access.
*  As a user, I want to have access to all the links, so I can connect to the website's social networks.
*  As a user, I want to create an account and login/logout, so I can interact with the website and community, access my account and close it on multiple devices.
*  As a user, I want to add new posts, edit and delete them, so I can upload my content and manipulate it if necessary.
*  As a user, I want to interact with the other posts, so I can give my opinion.


<h3>Scope</h3>

*  The website should be functional, easy to navigate and intuitive.
*  The frontend should be simple and present the content in a clear way.
*  Allow users to manipulate their content (CRUD Operations).
*  Allow logged in users to interact with other posts through comments.
*  Allow the user to create an account in order to upload content.
*  Use bootstrap to make the site responsive, and custom CSS and Java Script to complement.
*  Create a webpage application using the Django framework.

<h3>Structure</h3>

<p>Taste Coffee, will have fourth distinct pages for the first-time user.</p>

  *  Home page, Coffees ,Register, and Login.

<p>Unlogged users will be able to navigate through these four pages and will be able to see the details of each Coffee by clicking on its link. But they will not be able to interact.

When the user creates an account and is logged in, the following pages will be displayed.</p>

*  Home page, Coffees ,Logout, and My area.

<p>Logged-in users will be able to access the site completely. Being able to access the details of the coffes and interact with them.

He will be able to access his area (My Area) to add new posts, modify the ones already added, or delete them.</P>


<h3>Skeleton</h3>

<p>The wireframe was created using the Figma tool. During the elaboration of the wireframes, I added what the front end should look like.</p>

*  Wireframes

![Picture13](https://user-images.githubusercontent.com/93129370/187054440-43174423-f67c-4ad6-9017-77d10ed2aa70.png)

![Picture14](https://user-images.githubusercontent.com/93129370/187054463-e40a6163-73ec-4202-818e-721f2f697195.png)



<h3>Database diagram</h3>
<p>The base data for Taste Coffee starts from the logged in user who can create a Post Coffee .</p>



![diagram](https://user-images.githubusercontent.com/93129370/187052520-6b5c1494-b36c-4295-bb47-ef41a39ff28c.png)

<h3>Surface</h3>

*  Colours


![colors](https://user-images.githubusercontent.com/93129370/187049930-fc432acf-ba16-4e72-8100-75311b4fd897.png)


<h3>Typography</h3>

<p>The site's font was chosen from google fonts.</p>

<h2>Surface</h2>

<h3>Colour scheme</h3>

* The colors chosen to compose the website are the following.

* The colors white/black will be used for the background and to create contrast between the sections.

* The gray will be used in the forms and cards to stand out from the background.

* Orange will be used to highlight the nav bar/footer/buttons.

* Yellow will be used for title effects, and view more button.

* Bootstrap default colors were also used for some buttons on the forms.

<h2>Imagery</h2>

* For the Taste Coffee project, I selected images that can enhance the user's visual response and convey the idea of the website. 


<h1>Features</h1>

<h2>Existing Features</h2>


<h3>Favicon</h3>

* Favicon is loaded on every page.

<h3>Navbar</h3>

* Navbar that is present on all pages for user navigation through the website, is present the logo with the site name that redirects to the home page, the link to home page, a link to coffees (all coffees).
* If the user does not have an account or is logged out, links to signup (register a new account) and signin (for the user to log in) are available. user is logged in, the links are available to logout (confirmation page) and link to members (My area). 
* Navbar is responsive, for mobiles it automatically groups to drowdown menu.

![home](https://user-images.githubusercontent.com/93129370/187056562-67bdd135-b5b0-4731-97ad-750ac93483ea.jpeg)


<h3>Footer</h3>

* Is also present two links that redirect the users to the social networks of the page to increase their interaction with the community.

* The links present in the footer count with hover effect to increase the highlight of which selection will be executed with the click.

<h3>Hero image</h3>

* Present on the index page, and one of the first images that the user sees when he logs into the website, it has a background image of an  coffee.
 
 ![Picture4](https://user-images.githubusercontent.com/93129370/187056670-18cc8fb1-cd7e-4203-b2f0-a9135d12b838.png)


<h3>About section</h3>

* This section has a short introductory text about what is being made available on the website.

<h3>Sign out</h3>

* Registration page, with a simple form with the field for username, e-mail (optional) and for password twice, a button to register. A short text that calls who already has a registration to the login page.

![Picture8](https://user-images.githubusercontent.com/93129370/187056701-f6ea7224-f79d-4569-aa44-a74f0443dcc6.png)


<h3>Sign in</h3>

* Access page, with two fields to be filled in (username and password). a button to log in. A short text with a callout for those who don't have an account.

![Picture7](https://user-images.githubusercontent.com/93129370/187056687-27cd4c45-38b6-415a-8f03-42d8fddc7023.png)

<h3>Logout</h3>

* Page for logged in users who have selected the logout option.


<h3>User area</h3>

* Area for logged in users, display greeting text with user name, one button for action: add coffee.

![Picture10](https://user-images.githubusercontent.com/93129370/187056787-b88642fd-77d2-41c9-b8db-ac7657d7ed72.png)


* If the user tries to access the page with the url without being logged in, it shows a different screen saying that he must create an account or log in to his existing account.

<h3>My Area</h3>
* Page for logged in users that shows a list of the coffees added by the user.

<h3>Add coffee</h3>

* Page for logged in users that provides the form for adding a new coffee.

![Picture10](https://user-images.githubusercontent.com/93129370/187056787-b88642fd-77d2-41c9-b8db-ac7657d7ed72.png)

<h3>Edit Coffee</h3>
 
* Page for logged in users that allows editing of a previously added coffee, only the user himself can change it. 

![Picture11](https://user-images.githubusercontent.com/93129370/187056829-7927bb4d-6e8a-4328-82b3-19142bfd98a9.png)


<h3>Delete Coffee</h3>

* Page for logged in users that enables them to delete the information.

![Picture12](https://user-images.githubusercontent.com/93129370/187056840-fca8613d-3d6a-4b3b-aa47-674b7736e9d5.png)


<h3>Coffess</h3>

* Page shows all coffees added in the website, by default shows the most recent first. Each coffee is visible in a card with the following information (Name, brand and Origin).

![Picture5](https://user-images.githubusercontent.com/93129370/187056859-25b9ed83-921a-4f17-a59e-55a8a7152f9d.png)


<h3>View More</h3>

* Page with all coffee informations in more details.
* Not logged in user can only see the total of coffes and can not interact, can only read the comments and can not comment.
* Logged in user can see everything that the non logged in user can see, but he can interact with the page and he can send comments.

<h3>Comments</h3>

* The comments have the same layout for coffees. Only logged in users can comment. A message that the comment has been sent for approval will appear as soon as you submit the comment.


<h3>Features Left to Implement</h3>

* You will be able to evaluate the coffee and the favorite in addition to searching.
* The possibility for users to send private messages to other users, so they can make offers or communicate in a more practical way than comments.
* Add more functionalities in the user area like interaction notifications, more information options like profile (photo, description, interests).


<h2>User stories testing</h2>

<p>As a first time user</p>

* Easily understand the site's purpose.
    * The site's homepage background image and introduction paragraph quickly inform first time users of the site's purpose. This is then further expanded upon if the user scrolls to the 'How it Works' section of the homepage or visits the about us page.
    ![Picture4](https://user-images.githubusercontent.com/93129370/187054621-0041dd97-e8ea-4625-9f6e-a3cc8344abd9.png)


* Easily navigate to all relevant pages.
   * The site boasts an elegant, intuitive and adaptive navigation system on all screen sizes. Making it simple to traverse all pages.

  ![home](https://user-images.githubusercontent.com/93129370/187054737-6d6467e6-fcd6-4879-809b-a463d57075d3.jpeg)


* Easily find coffee details to allow me to make an informed decision.
   
   ![Picture5](https://user-images.githubusercontent.com/93129370/187054780-b18edf9c-43f8-4284-892b-97fdafa53d82.png)

  

* Create an account to store personal and purchase information.
   *  Once a user has been created they can navigate to the profile page. Here a user can manage their details  to view and edit them here.
   
   ![Picture11](https://user-images.githubusercontent.com/93129370/187054847-310dc0c5-caae-434b-a357-6fc783184e79.png)

   

* Purchase a subscription.
  * Selecting a plan from the subscriptions page will direct the user to the checkout page (if they are logged in, login page if not) and allow them to enter their details and purchase a subscription.


<h3>As a return user/customer -</h3>

* Login to my account.
   * Users can navigate to the login page from the navbar on any page. Entering their details here will log them in.

<h3>As an admin user -</h3>
* Log in to an admin account.
  * Admin users can navigate to the login page from the navbar on any page. Entering their admin credentials here will log them in.

 <h2>Responsive Design</h2>
 
<p>To test the responsive design of my site I checked each page in various sizes using Google Chrome's Dev tools. Chrome dev tools allows you to virtually scale your site to a variety of common device types and also allows you to input specific, custom display dimensions to test any screen size. Using this tool I was able to render each page in a variety of screen sizes and check the results. For each resolution I checked for:</p>

* Clearly legible text
* Consistent styling
* No blocked or hidden elements

 <p>Here are some screenshots demonstrating this for the site subscriptions page.</p>
 
* - Mobile (375-667px)
 
* - Tablet (768-1024px)
 
* - Desktop (1920-1080px)
 
 
 <h2>Code Validation</h2>
 
 <h3>HTML validation</h3>
 
 <p>All HTML was tested using Nu HTML Checker and returned no errors.</p>
 
 <h3>CSS validation</h3>

 <p>All custom CSS code was tested using the Jigsaw css validator and showed no errors relating to custom code. All errors were relating to the Materialize CDN CSS.</p>
 
 <h3>JS validation</h3>
 
<p>All Javascript code was tested using Beautify Tool Javascript validator and returned no errors.<p>

 <h3>Python validation</h3>
 
<p>All Python was tested and checked against pep8 standards using pylint in vscode and returned no errors.</p>
 
 <h2>Automated</h2>
 
 ![test](https://user-images.githubusercontent.com/93129370/187055541-7a0d1a1c-515a-4826-bcd4-6b312ad7da5b.jpeg)


<h2>Deployment</h2>

* To create this project I used GitHub and GitPod.
* I used the Code Institute Gitpod Full Template, clicking on the "Use this template" button. From there I created the repository on Github with my username.
* These commands were used for version control during project:
    * git status - to check the status of the files to be commited.
    * git add filename - to add files before committing.
    * git commit -m "message" - to commit changes to the local repository.
    * git push - to push all committed changes to the GitHub repository.

<h3>Deployment</h3>

<p> 1. Create Django project and app </p>

* I installed django using the command pip3 install 'django<4' gunicorn;
* I installed supporting database libraries dj_database_url and psycopg2, using pip3 install dj_database_url psycopg2;
* I installed Cloudinary library to upload the images, using pip3 install dj3-cloudinary-storage;
* I created the requirements.txt file using the command pip3 freeze --local > requirements.txt;
* I created my Django project with the command django-admin startproject project_name .;
* I created my Django app with the command python3 manage.py startapp app_name;
* I used the comands python3 manage.py makemigrations and python3 manage.py migrate;
* To test and run the project I used python3 manage.py runserver.

<p> 2. Create Heroku app </p>

* I opened the heroku website and logged into my account
* I created a new app with the project name, chose the region Europe
* I opened the Resources section and searched for Heroku Postgres and selected it
* I opened the Settings section and then Config VARS, after I initially added the keys needed to start development DATABASE_URL/SECRET_KEY/CLOUDINARY_URL;
* Still in Config VARS I added the following keys: PORT with a value of 8000 and DISABLE_COLLECTSTATIC with a value of 1;

<p> 3. Set up Django settings.py and necessary folders/files </p>

* Set up to connect the environment variables
         from pathlib import Path
         import os
         import dj_database_url
         from django.contrib.messages import constants as messages
         if os.path.isfile('env.py'):
         import env
         
* Inside INSTALLED_APPS I added the necessary apps

* For the database I replaced it with the following code

        DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
        
* For the static files I replaced it with the following code to conect to Cloudinary

      STATIC_URL = '/static/'
      STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
      STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
      STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

      MEDIA_URL = '/media/'
      DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
      
* Create a Procfile and add the following text

web: gunicorn autoclassic.wsgi

<h3> 4. Final deployment. </h3>

* In settings.py inside the Django project I changed DEBUG = False;
* Also in the settings.py file I added X_FRAME_OPTIONS = "SAMEORIGIN";
* In Heroku I went back to Settings > Config VARS and removed the DISABLE_COLLECTSTATIC var;
* In Heroku I navigated to the Deploy section;
* I clicked to connect to GitHub and searched for my repository for this project;
* I clicked on manual deploy to build the App;
* When finished, I clicked the View button, which redirected me to the live site.

<h2>Fork</h2>

* Forks let you make changes to a project without affecting the original repository. Follow this steps:
1. Go to the repository page, can be accessed here.
2. On top right, you select the Fork option and proceed.
3. A duplicate will be created inside your repository.

<h2>Clone</h2>

* Clone let you create an identical repository to the original. Follow this steps:
1. Go to the repository page, can be accessed here.
2. Click on code drop down menu.
3. Choose if you want to clone using HTTPS, SSH or GitHub CLI. Then select de copy button.
4. Open your Git Bash in your IDE.
5. Type git clone and then paste the URL you copied before.
6. Press Enter to create your clone.
         
         
<h2>Technologies and tools</h2>

<p> Programming languages used: Python 3.8, Java Script, HTML5 and CSS3. </p>

* Gitpod - Used to create/edit the code of the project.

* Github - Used to create repository, for version control and Agile project.

* Heroku - Used to deploy the project.

* Django - Used in the development of this project. Main python Framework.

      *The following python modules were used on this project:
      asgiref==3.5.2
           cloudinary==1.29.0
           dj-database-url==0.5.0
           dj3-cloudinary-storage==0.0.6
           Django==3.2.14
           django-allauth==0.51.0
           django-crispy-forms==1.14.0
           django-summernote==0.8.20.0
           gunicorn==20.1.0
           oauthlib==3.2.0
           psycopg2==2.9.3
           PyJWT==2.4.0
           python3-openid==3.2.0
           pytz==2022.1
           requests-oauthlib==1.3.1
           sqlparse==0.4.2
     
* Bootstrap - Used to . CSS/JS Framework for developing responsiveness and styling.

* PostgreSQL - Used as database for this project. Straight from Heroku.

* Cloudinary - Used to upload images and cloud hosting service.

* Jquery Ajax - Used to load more content at garage and events pages.

* Ludichart - Used to create the database diagram and agile images.

* Figma - Used to creat the wireframes.

* Coolors - Used to choice of colors and for the palette used in the README.

* Font Awesome - Used for the favourite icon.

* Bootstrap Icons - Used for all others icons.

* Favicon.io - Used to implement the favicon on the website.

* DevTools - Chrome - to assist in the development of the project.

* Lighthouse (Chrome Devtools) - Used to performance test.

* WAVE - Used to acecessibility test.

* PEP8 - Used to test/validate Python code.

* JShint - Used to test Java Script code.

* Jigsaw - Used to test CSS code.

* Validator - Used to test HTML code.

<h2>Credits</h2>

<h3>CODE</h3>

<p> I present here the sources of information that I used to develop the project and the applications contained therein. </p>

* [Code Institute](https://codeinstitute.net/ie/) 
* [Django Documentation](https://docs.djangoproject.com/en/4.1/)
* [Bootstrap Documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

<h3>Content</h3>

All images used to create the demo content for the site were selected from: Bazaart, Bing and Google Images. I thank the curatorship of the three sites for the extraordinary images.

<h3>Media</h3>

* The photos used for Hero (Home page) and placeholder images was taken from [Bazzart](https://www.bazaart.me/) [Bing](https://www.bing.com/images/details/%7B0%7D) [Google Images](https://images.google.com/)
* Text Reveal Effect [WEB CIFAR](https://www.youtube.com/channel/UCdxaLo9ALJgXgOUDURRPGiQ)
* Responsive Nav-bar [WEB CIFAR](https://www.youtube.com/channel/UCdxaLo9ALJgXgOUDURRPGiQ)
* All the icons from [Icons8](https://icons8.com/)

<h2>Acknowledgements</h2>

* Code Institute for all the support.
* Guido, my mentor for sharing knowledge and insights that broadened my vision of the project.
* The Slack community for sharing their expertise.
*  My wife and friends for believing in me.
