from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('shows',views.open_home),
    path('logout',views.logout),
    path('login',views.login),
    path('shows/new',views.create),
    path('add',views.add),
    path('shows/<int:id>',views.show_details),
    path('shows',views.shows),
    path('shows/<int:id>/edit',views.edit),
    path('update',views.update),
    path('shows/<int:id>/destroy',views.destroy),
    path('comment',views.add_comment),
    path('delete_comment',views.delete_comment),

]
