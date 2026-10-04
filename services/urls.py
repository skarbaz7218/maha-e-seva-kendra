from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "services/",
        views.service_list,
        name="service_list"
    ),

    path(
        "services/<int:service_id>/",
        views.service_detail,
        name="service_detail"
    ),

    path(
        "privacy-policy/",
        views.privacy_policy,
        name="privacy_policy"
    ),
    path(
    "terms-of-service/",
    views.terms_of_service,
    name="terms_of_service"
),
   
]