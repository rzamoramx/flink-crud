from rest_framework import routers
from .api import SymbolViewSet


router = routers.DefaultRouter()

router.register('v1/symbols', SymbolViewSet, 'symbols')

urlpatterns = router.urls
