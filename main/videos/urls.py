from django.urls import path
from . import views

urlpatterns = [
    path('video',views.video,name='video'),
    path('deliverance',views.deliverance_video,name='deliverance'),
    path('sermon',views.sermon_video,name='sermon'),
]
