from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Post


class PostListView(ListView):
    """
        ListView with a list of reviews

        In GET: Returns the main page of the site with a list of recent posts

        Template: index.html
        """
    template_name = 'posts/index.html'
    model = Post
    context_object_name = "posts"
    paginate_by = 6


class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post


