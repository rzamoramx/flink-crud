from rest_framework import routers
from .api import SymbolViewSet
from . import views
from django.urls import path


router = routers.DefaultRouter()

router.register('v1/symbol', SymbolViewSet, 'symbols')

urlpatterns = router.urls

urlpatterns.append(path('v1/function_view', views.function_view))
urlpatterns.append(path('v1/class_view', views.ClassView.as_view()))
urlpatterns.append(path('v1/messages_example', views.messages_example))
