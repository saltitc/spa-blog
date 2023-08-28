from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q
from .models import Post, Comment
from taggit.models import Tag
from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['common_tags'] = Post.tag.most_common()
        context['last_posts'] = Post.objects.exclude(slug=self.object.slug)[:5]
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(Post, slug=slug)
            comment = Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'posts/post_detail.html', context={
            'comment_form': comment_form
        })


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


class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Post.objects.filter(tag=tag)
        common_tags = Post.tag.most_common()
        return render(request, 'posts/tag.html', context={
            'title': f'#ТЕГ {tag}',
            'posts': posts,
            'common_tags': common_tags
        })
