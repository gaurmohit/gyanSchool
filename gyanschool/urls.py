from django.contrib import admin
from django.urls import path,include
from authh import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page,name='secret'),
    path('secret2', views.SecretPage.as_view(),name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'^oauth/', include('social_django.urls', namespace='social')),


    path('admin/', admin.site.urls),
]