from django.urls import path
from django.urls import include
from about import views
app_name = 'about'
urlpatterns = [
    path('', views.about, name='about'),
    

]