from api.views import CommentsViewSet, GroupsViewSet, PostsViewSet
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('posts', PostsViewSet, basename='posts')
router.register('groups', GroupsViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet, basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
