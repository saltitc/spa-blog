from django.urls import path

from .views import PostDetailView, PostListView, SearchResultsView, TagView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("blog/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("tag/<slug:slug>/", TagView.as_view(), name="tag"),
]
