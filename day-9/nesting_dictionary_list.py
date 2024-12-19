
# Training with nested dictionaries and lists

def add_new_country(new_country, new_country_visits, new_list_of_cities):
    travel_log.append({"country":  new_country,
                       "visits": new_country_visits,
                       "cities": new_list_of_cities
                       })
    # more clean
    # new_country_entry = {}
    # new_country_entry["country"] = new_country
    # new_country_entry["visits"] =  new_country_visits
    # new_country_entry["cities"] = new_list_of_cities
    # travel_log.append(new_country)



country = input()
visits = int(input())
list_of_cities = eval(input())

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": [ "Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": [ "Berlin", "Hamburg", "Stuttgart"]
    },

]

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
print(f"My favourite city was {travel_log[2]['cities'][0]}")