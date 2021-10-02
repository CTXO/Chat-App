from django.urls import path
from .views import show_all, create_user, delete_user, send_message, read_chat, add_contact, delete_contact, show_contacts
urlpatterns = [
    path('index/', show_all),
    path('create/', create_user),
    path('delete/', delete_user),
    path('send/', send_message ),
    path('read/', read_chat ), #laterrr
    path('contact/add/', add_contact),
    path('contact/delete/', delete_contact),
    path('contact/index/', show_contacts),
    
]
