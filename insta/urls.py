from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.indexPage, name='home'),
    path('profile/', views.profile,name='profile'),
    url('edit/', views.edit_profile,name='edit_profile'),
    url('user/',views.search_username,name='search_username'),
    url('image/', views.upload_image,name='upload_image'),
    url('likes/(\d+)/' , views.image_likes, name='likes'),
    url('new_comment/(\d+)/' ,views.add_comment,name='Comments'),
    path('post/', views.create_post,name='create_post'),
    path('registration/', views.registerPage, name="registration"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)