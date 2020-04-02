from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login, name='login'),
    path('process_login', views.process_login, name='process_login'),
    path('new', views.new, name='new'),
    path('process_new',views.process_new,name='process_new'),
    path('create', views.create, name='create'),
    path('<int:number>', views.blog, name='blog'),
    path('<int:number>/entries', views.process_new_entry, name='process_new_entry'),
    path('<int:number>/edit', views.edit, name='edit'),
    path('<int:number>/delete', views.delete, name='delete')
]
