from django.urls import path
from . import views
urlpatterns = [
    path('',views.views_index,name="index"),
    path('index/',views.views_index,name="index"),
    path('blog/',views.blog,name="blog"),
    #path('blog/',views.blog,name="blog"),
]

