from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'news'

urlpatterns = [
                  path(r'', views.index, name='index'),
                  re_path(r'^([0-9]+)/$', views.detail, name='detail'),
                  re_path(r'^register/$', views.RegisterFormView.as_view()),
                  re_path(r'^login/$', views.LoginFormView.as_view()),
                  re_path(r'^logout/$', views.LogoutView.as_view()),
                  re_path(r'^profile/([0-9]+)/$', views.profile, name='profile'),
                  re_path(r'^post_img/$', views.post_img, name='post_img'),
                  re_path(r'^([0-9]+)/post/$', views.post, name='post'),
                  re_path(r'^([0-9]+)/msg_list/$', views.msg_list, name='msg_list'),
                  re_path(r'^([0-9]+)/post_mark/$', views.post_mark, name='post_mark'),
                  re_path(r'^([0-9]+)/get_mark/$', views.get_mark, name='get_mark'),
                  re_path(r'^password-change/', views.PasswordChangeView.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
