from django.urls import include, path  
from rest_framework import routers 
from .views import *

router = routers.DefaultRouter()  
router.register("view", UserViewSet)
# router.register('cats', CategoryViewSet)
router.register("des", DescriptionViewSet)
router.register(r"cats", CategoryViewSet, basename='cat')
# router.register("Product", ProductViewSet)

  
#  URL Path for rest_framework 
urlpatterns = [ 
    path('', include(router.urls)),  
] 