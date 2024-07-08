
from django.contrib import admin
from django.urls import path
from news_blog.views import news_blog_view, about_me_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news_blog/', news_blog_view),
    path('about_me/', about_me_view),
]
