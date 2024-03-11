from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.predict_crop, name='predict_crop'),
]
