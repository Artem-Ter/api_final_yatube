from rest_framework.routers import SimpleRouter

from django.urls import path, include

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('', include('djoser.urls.jwt')),
]
