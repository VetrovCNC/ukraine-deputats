from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'deputats', views.DeputatViewSet, 'deputats')

app_name = 'api'
urlpatterns = [
    path('v1/', include(router.urls)),
]