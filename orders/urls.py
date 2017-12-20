from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^create/$',
            views.order_create,
            name='order_create'),
        url(r'^error_paid/$',
            views.error_paid,
            name='error_paid')
]

