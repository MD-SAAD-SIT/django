from django.shortcuts import render


def form_view(request):
    return render(request, "form.html")


def display_view(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "age": request.POST.get("age"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
            "address": request.POST.get("address"),
        }
        return render(request, "display.html", data)
