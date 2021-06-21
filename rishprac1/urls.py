"""rishprac1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rk01 import views as cv
from rk02 import views as fv

# using cv & fv has renamed views from multiple apps to help django to select correct view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn/', cv.learn_django),
    path('learn/var/', cv.learn_var),
    path('learn/math/', cv.learn_math),
    path('learn/math/format', cv.learn_format),
]

# option 2 to mention urls is as follows
# from rk01.views import learn_django
# urlpatterns = [
    #path('learn/', learn_django),
#]