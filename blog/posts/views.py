from django.views.generic.list import ListView
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
