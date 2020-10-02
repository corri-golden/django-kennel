from django.contrib import admin
from django.urls import include, path
from kennelapp.models import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kennelapp.urls'))
]
