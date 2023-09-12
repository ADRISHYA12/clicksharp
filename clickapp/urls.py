from django.urls import path
from clickapp import views
urlpatterns=[
    path('index/',views.index,name="index"),
    path('table/',views.table,name="table"),
    path('form/', views.form,name="form"),
    path('addphotographers/', views.addphotographers,name="addphotographers"),
    path('savephitod/', views.savephitod,name="savephitod"),
    path('display/', views.display,name="display"),
    path('edit/<int:dataid>/', views.edit, name="edit"),
    path('update/<int:dataid>/', views.update, name="update"),
    path('delete/<int:dataid>/', views.delete, name="delete"),
    path('cat/', views.cat, name="cat"),
    path('savcat/', views.savcat, name="savcat"),
    path('displaycat/', views.displaycat, name="displaycat"),
    path('editc/<int:dataid>/', views.editc, name="editc"),
    path('updatec/<int:dataid>/', views.updatec, name="updatec"),
    path('deletec/<int:dataid>/', views.deletec, name="deletec"),
    path('single/', views.single, name="single"),
    path('saveitm/', views.saveitm, name="saveitm"),
    path('display_single/', views.display_single, name="display_single"),
    path('edit_single/<int:dataid>/', views.edit_single, name="edit_single"),
    path('updatesinglepage/<int:dataid>/', views.updatesinglepage, name="updatesinglepage"),
    path('delete_single/<int:dataid>/', views.delete_single, name="delete_single"),
    path('add_service/', views.add_service, name="add_service"),
    path('saveservice/', views.saveservice, name="saveservice"),
    path('display_service/', views.display_service, name="display_service"),
    path('edit_service/<int:dataid>/', views.edit_service, name="edit_service"),
    path('update_service/<int:dataid>/', views.update_service, name="update_service"),
    path('delete_service/<int:dataid>/', views.delete_service, name="delete_service"),
    path('display_contact/', views.display_contact, name="display_contact"),
    path('delete_contact/<int:dataid>/', views.delete_contact, name="delete_contact"),
    path('display_appoinment/', views.display_appoinment, name="display_appoinment"),
    path('delete_appoinment/<int:dataid>/', views.delete_appoinment, name="delete_appoinment"),
    path('', views.loginggpage, name="loginggpage"),
    path('loginsucc/', views.loginsucc, name="loginsucc"),
    path('logoutadmin/', views.logoutadmin, name="logoutadmin"),



]
