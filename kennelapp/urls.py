from django.urls import include, path
from .views import *
from django.urls import path


app_name = "kennelapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
    path('cats/', cat_list, name='cats'),
    path('cat/form', cat_form, name='cat_form'),
    path('caretakers/', caretaker_list, name='caretakers'),
    path('kennels/', kennel_list, name='kennels'),
    path('kennel/form', kennel_form, name='kennel_form'),
    path('cats/<int:cat_id>/', cat_details, name='cat'),
    path('kennels/<int:kennel_id>/', kennel_details, name='kennel'),
    path('caretakers/<int:caretaker_id>/', caretaker_details, name='caretaker'),
    path('cats/<int:cat_id>/form/', cat_edit_form, name='cat_edit_form'),

]