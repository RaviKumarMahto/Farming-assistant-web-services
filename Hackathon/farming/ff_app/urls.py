
from django.urls import path, include
from . import views
from django.urls import path
from ff_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index', views.index),
    
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('add_post', views.add_post, name='add_post'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout'),
    path('blogs',views.blogs,name='blogs'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('services', views.services),
    path('contact_us', views.contact),
    path('about', views.about),
    path('order', views.order_now)



]
