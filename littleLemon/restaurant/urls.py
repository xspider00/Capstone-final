from django.contrib import admin 
from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token
from .views import sayHello, index, MenuView, SingleMenuItemView

  
urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('',index, name='index'),
    path('menu/items', MenuView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]