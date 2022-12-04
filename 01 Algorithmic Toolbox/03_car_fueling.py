from sys import stdin


def min_refills(distance: int, tank: int, stops: list) -> int:
    tank_full = tank
    number_of_stops = 0
    i = 0
    stops.append(distance)
    if not stops and (distance > tank):
        return -1
    elif tank < stops[0]:
        return -1
    else:
        stops_distance = []
        previous_stop = 0
        for current_stop in stops:
            stops_distance.append(current_stop-previous_stop)
            previous_stop = current_stop
        for stop in stops_distance:
            if stop > tank:
                return -1
        stops_distance.pop()
        while distance > 0:
            if distance <= tank:
                return number_of_stops
            while i < len(stops_distance):
                if tank > stops_distance[i]:
                    tank -= stops_distance[i]
                    distance -= stops_distance[i]
                    if distance <= 0:
                        return number_of_stops
                    i += 1
                elif tank == stops_distance[i]:
                    tank -= stops_distance[i]
                    distance -= stops_distance[i]
                    if distance <= 0:
                        return number_of_stops
                    number_of_stops += 1
                    tank = tank_full
                    i += 1
                elif tank < stops_distance[i]:
                    number_of_stops += 1
                    tank = tank_full
                    tank -= stops_distance[i]
                    distance -= stops_distance[i]
                else:
                    return number_of_stops
    return number_of_stops




if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
