from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contacts.views import ContactView


router = DefaultRouter()
router.register('contact', ContactView, basename='contact')


urlpatterns = [
    path('', include(router.urls)),

]
