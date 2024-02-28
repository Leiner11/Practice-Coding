from django.urls import path
from . import views

urlpatterns = [
    #/genres/
    path('',views.index.as_view(),name="index"),

    #genre/1
    path('<pk>/',views.details.as_view(),name="details")
]