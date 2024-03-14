from django.contrib import admin
from django.urls import path, include

# Define the urlpatterns for the project
urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Include the URLs from the candidates app
    path('candidates/', include('candidates.urls')),
]
