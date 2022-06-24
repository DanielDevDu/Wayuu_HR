from rest_framework import routers
from legal.api.views import *

router = routers.DefaultRouter()
router.register('salaries', SalaryViewSet, 'salaries')
router.register('vacation', VacationViewSet, 'vacation')
router.register('social_security', SocialSecurityViewSet, 'social_security')

urlpatterns = router.urls