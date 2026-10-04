from django.shortcuts import render, get_object_or_404
from .models import Service


def home(request):

    # Home page pe specific services dikhane ke liye
    # Aadhar Card, Voter ID, Pan Card — is order me
    featured_names = [
        "Aadhar Card",
        "Voter ID",
        "PAN Card",
    ]

    services = Service.objects.filter(
        is_active=True,
        name__in=featured_names
    )

    # Custom order maintain karne ke liye
    ordered_services = []
    for name in featured_names:
        for service in services:
            if service.name == name:
                ordered_services.append(service)

    # Agar koi service missing hai, to baaki services se fill karo
    if len(ordered_services) < 3:
        other_services = Service.objects.filter(
            is_active=True
        ).exclude(
            name__in=featured_names
        ).order_by("-created_at")

        for service in other_services:
            if len(ordered_services) >= 3:
                break
            ordered_services.append(service)

    return render(
        request,
        "services/home.html",
        {"services": ordered_services}
    )


def service_list(request):
    services = Service.objects.filter(
        is_active=True
    ).order_by("-created_at")

    return render(
        request,
        "services/service_list.html",
        {"services": services}
    )


def service_detail(request, service_id):
    service = get_object_or_404(
        Service,
        id=service_id,
        is_active=True
    )

    related_services = Service.objects.filter(
        is_active=True
    ).exclude(
        id=service_id
    ).order_by("-created_at")[:4]

    return render(
        request,
        "services/service_detail.html",
        {
            "service": service,
            "related_services": related_services,
        }
    ) 
def privacy_policy(request):
        return render(
            request,
            'services/privacy_policy.html'
        )
def terms_of_service(request):
    return render(
        request,
        'services/terms_of_service.html'
    )



 
    