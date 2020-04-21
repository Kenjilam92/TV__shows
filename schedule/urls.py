from django.urls import path
from . import views
urlpatterns=[
    path('',views.homeroute),
    path('shows',views.shows),
    path('shows/new',views.new),
    path('shows/create',views.create),
    path('shows/<x>',views.read),
    path('shows/<x>/update',views.update),
    path('shows/<x>/edit',views.edit),
    path('shows/<x>/delete',views.delete),
]