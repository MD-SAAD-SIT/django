from django.shortcuts import render


def home(request):
    name = ""
    if request.method == "POST":
        name = request.POST.get("name")
    return render(request, "home.html", {"name": name})
