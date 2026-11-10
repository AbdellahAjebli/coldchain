from django.shortcuts import render

from .models import Dht11

def dht_view(request):
    readings = list(Dht11.objects.order_by("-date")[:24])
    readings.reverse()
    latest_reading = readings[-1] if readings else None
    chart_readings = [
        {
            "date": reading.date.isoformat(),
            "temperature": reading.temperature,
            "humidity": reading.humidity,
        }
        for reading in readings
    ]
    return render(
        request,
        "DHT/dashboard.html",
        {
            "readings": readings,
            "latest_reading": latest_reading,
            "chart_readings": chart_readings,
        },
    )