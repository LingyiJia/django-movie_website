from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about1/', views.about1, name='about1'),
    path('about2/', views.about2, name='about2'),
    path('about3/', views.about3, name='about3'),
    path('about4/', views.about4, name='about4'),
    path('about5/', views.about5, name='about5'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    # path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search'),
    path('add_contact/', views.add_contact, name='add_contact'),
]