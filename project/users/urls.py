from django.urls import path 
from users.views import Index
urlpatterns = [
   path('',Index.as_view(),name="index"),
   

]