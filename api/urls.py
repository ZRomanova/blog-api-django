from django.urls import path
from . import views
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()

router.register(r'users', views.UserView)
router.register(r'posts', views.PostView)
router.register(r'comments', views.CommentView)
router.register(r'categories', views.CategoryView)

urlpatterns = [
    path('api/', include(router.urls)),
]
