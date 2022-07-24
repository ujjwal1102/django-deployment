"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# from django.conf.urls import patterns,url
# from django.conf.urls import url
from django.urls import include,path
from django.contrib import admin
# from NewApp import views
from first_project import views
# from service import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('homepage/',views.homepage),
    path('books/',views.books),
    path('research/',views.research),
    path('signup/',views.signup),
    path('login/',views.login,name='form_name'),
    path('userform/',views.userform)


    # path('userform/',views.userform),
    # path('calulater/',views.calculater)
    # path('details/<slug:details>',views.myDetail),
    # path('steve-jobs/',views.steve_jobs,name = "jobs"),
    # path('aboutus/',views.aboutus),

    
]

