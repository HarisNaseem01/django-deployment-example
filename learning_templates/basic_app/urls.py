from django.urls import path
from basic_app import views 

app_name = 'basic_app'

urlpatterns= [
    path('relative/',views.relative,name='ralative'),
    path('other/',views.other,name='other'),
]