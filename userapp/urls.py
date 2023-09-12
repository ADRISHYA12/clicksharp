from django.urls import path
from userapp import views
urlpatterns=[

    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('loginfunction/', views.loginfunction,name="loginfunction"),
    path('savereg/', views.savereg, name="savereg"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('service/', views.service, name="service"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('price/', views.price, name="price"),
    path('appoinment/', views.appoinment, name="appoinment"),
    path('save_appoinment/', views.save_appoinment, name="save_appoinment"),
    path('singlephoto/<catname>', views.singlephoto, name="singlephoto"),
    path('download/<int:dataid>/', views.download, name="download"),


]
