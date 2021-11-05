from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

# to create RSS feeds feature in blog application

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list') #to generate url  
    description = 'New posts of my blog.'

def items(self):
    return Post.published.all()[:5]

def item_title(self, item):
    return item.title

def item_description(self, item):
    return truncatewords(item.body, 30)