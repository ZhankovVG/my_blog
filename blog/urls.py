from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostView.as_view(), name='main'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('review/<int:pk>/', views.AddComments.as_view(), name='comments'),
]
