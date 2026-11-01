rivers = {"nil": "mesir", "amazon": "amerika selatan", "kapuas": "indonesia"}
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")
print("\nNama sungai:")
for river in rivers.keys():
    print(river.title())

print("\nNegara/wilayah:")
for country in rivers.values():
    print(country.title())