from django.shortcuts import render


def resume_view(request):
    return render(request, "index.html")


def portfolio_view(request):
    return render(request, "portfolio-details.html")
