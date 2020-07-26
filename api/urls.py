from django.conf.urls import url, include
from rest_framework import routers
from .views import EntryViewSet, UserViewSet, hook_receiver_view, auth_view



router = routers.DefaultRouter()
router.register(r'entry', EntryViewSet)
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^hooks/', hook_receiver_view.as_view(), name='hook_receiver_view'),
    url(r'^aauth/', auth_view.as_view(), name='aauth'),

]