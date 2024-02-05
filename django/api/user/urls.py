from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'view_users', views.UserViewSet)
router.register(r'view_groups', views.GroupViewSet)
# router.register(r'user_detail', views.user_detail, basename='user_detail')


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]

urlpatterns += router.urls