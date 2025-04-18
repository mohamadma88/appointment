from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('account/', include('account.urls')),
    path('article/', include('article.urls')),
    path('appointment/', include('appointment.urls')),
    path('doctor/', include('doctor.urls')),

]
