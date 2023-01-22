
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("admin/", admin.site.urls, name = 'adminpage'),
    path('', include('idiosaneapp.urls')),
    path('api/', include('api.urls'))

]
