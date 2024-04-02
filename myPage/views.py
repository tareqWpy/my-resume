from django.shortcuts import render


def resume_view(request):
    context = {
        "full_name": "Taregh Khaleghi",
        "email": "taregh.khaleghi1381@gmail.com",
        "phone_number": "0938 345 1445",
        "address": "Iran - Gilan - Somesara - Tolomato - Hendkhale - Danesh Alley - No. 5",
    }
    return render(request, "index.html", context)
