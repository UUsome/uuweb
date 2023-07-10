"""uuweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

#from django.views.static import serve
#from uuweb.settings import MEDIA_ROOT

from django.contrib import admin
from django.urls import path, include # add include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('media/<path>', serve, {"document_root": MEDIA_ROOT}),
    path('', include('system.urls')), # add
    path('', include('dailyreport.urls')), # add
    path('', include('blog.urls')),
    path('', include('testuu.urls')), # add
]

# path('blog/', include(('blog.urls', 'blog'), namespace='blog')),