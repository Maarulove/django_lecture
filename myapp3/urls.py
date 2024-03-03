from django.urls import path
from .views import hello, Hello, my_views, Temlif, view_for, author_get, Posts

urlpatterns = [
    path('hello/', hello, name="hello"),
    # path("hello_cl/", Hello.as_view(), name='Hello_cl'),
    # path("my_views/", my_views, name="index"),
    # path("if/", Temlif.as_view(), name="templ"),
    # # path("for/", view_for.as_view(), name="templ_for"),
    # path("author/<int:author_id>/", author_get, name="templ_for"),
    # path("post/<int:post_id>/", Posts, name="templ_for"),

]
