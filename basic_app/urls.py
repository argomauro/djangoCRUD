from django.contrib import admin
from django.urls import path, re_path
from basic_app import views
app_name = "basic_app"
urlpatterns = [
    path('', views.indexApp, name='indexApp'),
    path('', views.indexHome, name='indexHome'),
    #NAVIGAZIONE DEI DETTAGLI DELLA SCUOLA
    path('scuola/list',views.SchoolListView.as_view(), name='listScuola'),
    path('scuola/create',views.SchoolCreateView.as_view(), name='createScuola'),
    path('scuola/update/<pk>',views.SchoolUpdateView.as_view(), name='updateScuola'),
    path('scuola/delete/<pk>',views.SchoolDeleteView.as_view(), name='deleteScuola'),
    path('scuola/detail/<pk>',views.SchoolDetailView.as_view(), name='detailScuola'),
    #NAVIGAZIONE DEI DETTAGLI DEGLI STUDENTI
    path('studente/detail/<pk>',views.StudentDetailView.as_view(), name='detailStudent'),
    path('studente/update/<pk>',views.StudentUpdateView.as_view(), name='updateStudent'),
    path('studente/delete/<pk>',views.StudentDeleteView.as_view(), name='deleteStudent'),
]
