
from django.contrib import admin
from django.urls import path, include
from final_project_coder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppFinal.urls')),
]
