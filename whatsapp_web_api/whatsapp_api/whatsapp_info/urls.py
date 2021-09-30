from django.urls import path
from .import views

urlpatterns = [
    path('',views.api_view,name='apiview'),
    path('createdata/',views.Create_Api_1,name='createdata'),
    path('showall/',views.showall,name='showall'),
    # path('show_phone_number/<int:pk>',views.show_phone_number,name = 'showphonenumber'),


]