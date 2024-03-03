from django.urls import path
from .views import total_in_view, total_in_db, total_in_template

urlpatterns = [
    path('view/', total_in_view, name="total_view"),
    path('templ/', total_in_template, name="total_templates"),
    path('db/', total_in_db, name="total_db"),
    
]
