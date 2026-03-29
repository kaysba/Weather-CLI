from rich.table import Table
from rich.console import Console


def find_temperature_color(temp):
    if temp < 0:
        color = "cyan"
    elif temp < 15:
        color = "blue"
    elif temp < 25:
        color = "green"
    else:
        color = "red"
    return color


def find_wind_color(wind):
    if wind < 28:
        color = "green"
    elif wind < 72:
        color = "orange"
    else:
        color = "red"
    return color

def display(data):

    if data["cod"] != 200:
        print(f"Erreur : {data['message']}")
        exit(2)
    else:
        name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        console = Console()
        table = Table(title=f"Weather : {name}, {country}")
        table.add_column("Info", style="bold", width=22, no_wrap=True)
        table.add_column("Value", width=30)

        temp_color = find_temperature_color(temperature)
        wind_kmh = round(wind * 3.6, 1)
        wind_color = find_wind_color(wind_kmh)

        table.add_row("[red]TEMPERATURE[/red]", f"[{temp_color}]{temperature}°C (feels {feels_like}°C)[/{temp_color}]")
        table.add_row("[yellow]WEATHER[/yellow]", weather)
        table.add_row("[blue]HUMIDITY[/blue]", f"{humidity}%")
        table.add_row("[white]WIND[/white]", f"[{wind_color}]{wind_kmh} km/h[/{wind_color}]")

        console.print(table)