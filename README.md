# Blog Application

A simple blog application  

# Features Implemented   
* Functionality to do CRUD Operations for a blog post  
* Customizing the administration site  
* Pagination for splitting the list of blog posts across several pages  
* Sharing the post by email  
* Adding comments to a blog posts  
* Feature to add tags for blog posts and searching blogs on the basis of tags  
* Recommending similar blog posts  
* Finding Top k Latest posts and Most commented Posts  
* Adding Sitemaps to the site 

# Next Steps

# Installation

1. Install `python 3.8.5` and create virtual environment in a project folder by `virtualenv myenv`  
2. Execute `git clone <project remote path>` in the folder    
3. Run `pip install -r requirements.txt` to install all library dependencies  
4. Execute `cd mysite` to enter mysite directory  
5. Execute `python manage.py runserver` to start the django server  
6. The Blog appplication will be running at `http://127.0.0.1:8000/`  
7. The admin site will be running at `http://127.0.0.1:8000/admin` and can be logged in using credentials present in admin_config.ini file
