from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from example import views

router = DefaultRouter()
# router.register(r'posts', views.PostViewSet)
# router.register(r'comments', views.CommentViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
