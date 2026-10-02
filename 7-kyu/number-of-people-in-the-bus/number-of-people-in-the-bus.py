def number(bus_stops):
    return sum([stop[0] for stop in bus_stops]) - sum([stop[1] for stop in bus_stops])