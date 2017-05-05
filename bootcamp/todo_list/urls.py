from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import ListViewset

router = DefaultRouter()
router.register(r'',ListViewset)
urlpatterns = [
	url(r'^', include(router.urls)),
]