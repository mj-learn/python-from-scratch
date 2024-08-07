# Nesting a List in a List
# [{Dictionary}, {Dictionary}, "string", int, [List], {Dictionary}, ...]
abc = ["A", "B", ["C", "D"]]  # Not effective


# Nesting a List in a Dictianary
# {Key: [List], Key2: {Dictionary}, Key3: "String", Key4: int, Key5: {Dictionary}, Key6: [List], ...}
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]
