from django.shortcuts import render
import requests

API_KEY = "0c362be71c1e45a5b73f4f044d45c5e6"


def home(request):
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.POST['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            }
        else:
            error = "Invalid city name. Please try again."

    return render(request, "home.html", {"weather": weather_data, "error": error})
