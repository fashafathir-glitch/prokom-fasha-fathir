cities = {
    "yogyakarta": {"country": "Indonesia", "population": 373000, "fact": "dikenal dengan budaya Jawa"},
    "tokyo": {"country": "Jepang", "population": 14000000, "fact": "memiliki jaringan kereta yang luas"},
    "paris": {"country": "Prancis", "population": 2100000, "fact": "dikenal dengan Menara Eiffel"},
}
for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"  Negara: {info['country']}")
    print(f"  Populasi (perkiraan): {info['population']:,}")
    print(f"  Fakta: {info['fact']}")
