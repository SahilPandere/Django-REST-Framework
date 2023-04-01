from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]