from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q
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
    """
        DetailView with detailed descriptions of posts

        In GET: Returns a page with a detailed description of the post

        Template: post_detail.html
    """
    template_name = 'posts/post_detail.html'
    model = Post


class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'posts/search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })
