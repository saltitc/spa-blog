from django.urls import path
from .views import PostListView, PostDetailView, SearchResultsView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]