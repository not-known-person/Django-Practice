"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_project import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.homepage, name="home"),
    path('admin/', admin.site.urls),
    path("about",views.about , name="about"),
    path("formdata",views.formData , name="formdata"),
    path("course/<int:courseid>",views.course,name="course"),
    path("item/<int:id>",views.item,name="item"),
    path("form",views.userpage,name="form"),
    path("car",views.getcar,name="car"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    # path("carData",views.carData,name="carData")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
