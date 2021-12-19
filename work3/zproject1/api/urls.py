from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration_view,name='apiOverview'),
    path('login/', views.login, name='login'),

    path('userLocUpdate/<str:pk>/', views.userLocUpdate, name = 'userLocUpdate'),
    path('getuserLoc/<str:pk>/', views.getuserLoc, name = 'getuserLoc'),
    path('getusersLoc/', views.getusersLoc, name="getusersLoc"),
    # path(),

    path('stores/',          views.getStores, name='getStores'),
    path('storeItems/',      views.getStoreItems, name='getStoreItems'),

    path('store/<str:pk>/',          views.getStore, name='getStore'),
    path('storeItem/<str:pk>/',      views.getStoreItem, name='getStoreItem'),
    
    # path('userHistory/<str:pk>/',       views.userHistory, name='userHistory'),
    path('userHistory/',       views.userHistory, name='userHistory'),
    path('getusersHistory/', views.getusersHistory, name = "getusersHistory"),
    path('getuserHistory/', views.getuserHistory, name= "getuserHistory"),

    path('', views.apiOverview,name='apiOverview'),
     
     path('boardlocs/',views.getboardlocs, name="getboardlocs"),
     
     path('getboardAdv/', views.getboardAdv, name = "get_board_Adv")

]
