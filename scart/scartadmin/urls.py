from os import name
from django.urls import path
from . import views


app_name = 'admin'
urlpatterns = [
    path('login/',views.adminLoginview,name='login'),
    path('',views.adminHomeview,name='home'),
    path('logout/',views.logout,name='logout'),
    path('<int:user_id>/detail',views.detailView,name='detail'),
    path('<int:user_id>/detail/edit',views.userDetailUpdate,name='edit_detail'),
    path('<int:user_id>/detail/delete',views.userDetaildelete,name='delete_user')


]   