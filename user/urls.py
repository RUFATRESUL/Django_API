from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('directory/',views.DirectorListAV.as_view(),name='director_list'),
    path('directory/<int:pk>/',views.DirectorDetailAV.as_view(),name='director_detail'),
    # path('customer-login/',auth_views.obtain_auth_token,name='customer-login')
    path('customer-login/',views.customer_login,name='customer-login'),
    path('customer-register/',views.customer_register,name='customer-register'),
    path('director-login/',views.director_login,name='director-login'),
    path('director-register/',views.director_register,name='director-register'),
    path('admin-login/',views.admin_login,name='admin-login'),
 
    # path('detail_comment/<int:pk>/',views.CommentDetailAPIView.as_view(),name='detail_comment')

    

]

