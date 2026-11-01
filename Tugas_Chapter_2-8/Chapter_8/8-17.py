def describe_pet(animal_type, pet_name):
    """Tampilkan informasi sederhana tentang hewan peliharaan."""
    print(f"\nSaya punya {animal_type}.")
    print(f"Nama {animal_type} saya adalah {pet_name.title()}.")

describe_pet("hamster", "harry")
describe_pet("kucing", "luna")
