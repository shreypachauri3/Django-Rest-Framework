from django.urls import path
from home.views import (home,HandleView)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns=[path('',home,name='home'),
 path('get-token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('get-refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify', TokenVerifyView.as_view(), name='token_verify'),
    path('todo/<str:author>',HandleView.as_view())
]
