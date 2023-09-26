from django.urls import path
from . import views

urlpatterns= [
    path("", views.home, name="home"),  
    path("about/", views.about, name="about"),  
    path("help/", views.help, name="help"),  
    # path("contact/", views.contact, name="contact"),  
    # path("<str:name>", views.view1, name="view1"),  
]

#sends to the right view according to the path recieved (in this case everything will go to index- view we defined)