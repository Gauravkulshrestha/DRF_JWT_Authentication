from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)
from rest_framework.routers import DefaultRouter
from api.views import ItemModelViewSets

router = DefaultRouter()

router.register('itemapi',ItemModelViewSets, basename='item_api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='get_token'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify_token'),
]
