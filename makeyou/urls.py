"""makeyou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from django.conf.urls.static import static
from django.conf import settings
from aboutme import views as make_views

urlpatterns = [
    url(r'^mypage/result/$', make_views.result, name="result"),
    url(r'^mypage/templates/$', make_views.templates, name="templates"),
    url(r'^mypage/edit/$', make_views.edit, name="edit"),
    url(r'^mypage/join/$', make_views.join, name="join"),
    url(r'^mypage/main/$', make_views.main, name="main"),
    url(
        r'^login/$', django_login,
        {'template_name': 'login.html'}, name="login_url"
    ),
    url(
        r'^logout/$', django_logout,
        {'next_page': '/login/'}, name="logout_url"
    ),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)