person1 = {"first_name": "fasha", "last_name": "fathir", "age": 19, "city": "yogyakarta"}
person2 = {"first_name": "alya", "last_name": "putri", "age": 20, "city": "bandung"}
person3 = {"first_name": "bima", "last_name": "saputra", "age": 21, "city": "jakarta"}
people = [person1, person2, person3]
for person in people:
    print("\nInformasi orang:")
    for key, value in person.items():
        print(f"{key}: {value}")
