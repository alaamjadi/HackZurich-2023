import hashlib

input_data = [
    {"name": "Carole", "surname": "Erni", "IBAN": "CH0214047068029644243"},
    {"name": "Anita", "surname": "Hofer", "IBAN": "CH4407701560939254166"},
    {"name": "Malin", "surname": "Eugster", "IBAN": "CH6540665316776472731"},
    {"name": "Corinna", "surname": "Tobler", "IBAN": "CH7398802571774599041"},
]


def pseudonymize(data):
    # Generate a pseudonymized ID based on name and surname
    m = hashlib.md5()
    m.update((data["name"] + data["surname"]).encode("utf-8"))
    pseudonymized_id = m.hexdigest()

    return {
        "ID": pseudonymized_id[:8],  # Taking the first 8 characters for brevity
        "IBAN": data["IBAN"],
    }


# Generate pseudonymized client data
pseudonymized_clients = [pseudonymize(entry) for entry in input_data]

# Display the pseudonymized data
for client in pseudonymized_clients:
    print(f"ID: {client['ID']}, IBAN: {client['IBAN']}")
