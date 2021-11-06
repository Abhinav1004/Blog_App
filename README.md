# Blog Application

A blog application having the feature to create,update,read and delete the blogs.It gives user functionality to share the particular post on email,commment on blog posts,and add associated tags to a particular blog which has been later used to make the list of most commented blog posts and recommend similar blog posts on the basis of tags assigned.It has been made using Django, leveraging it's powerful features in designing complex web application.

The blog also has the feature for searching and ranking the corresponding search results using features like how often the query terms appear in the document, how close together the terms are in the document, and how important the part of the document is where they occur.

### Tech Stack  

 **Backend** Django   
 **Front End** HTML,CSS,Bootstrap,JavaScript  
 **Database** Postgres   


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
* Added Search Feature to Blog
* Adding Stemming,Ranking and Trigram Similarity Advanced Search features 


# Next Steps  
* Adding a Text Editor with advanced features  
* Improving the UI of the application  

# Installation

1. Install `python 3.8.5` and create virtual environment in a project folder by `virtualenv myenv`  
2. Execute `git clone <project remote path>` in the folder    
3. Run `pip install -r requirements.txt` to install all library dependencies  
4. Execute `cd mysite` to enter mysite directory  
5. Execute `python manage.py runserver` to start the django server  
6. The Blog appplication will be running at `http://127.0.0.1:8000/`  
7. The admin site will be running at `http://127.0.0.1:8000/admin` and can be logged in using credentials present in admin_config.ini file
