def make_sandwich(*items):
    print("Sandwich dengan isi:")
    for item in items:
        print(f"- {item}")
make_sandwich("keju", "tomat")
make_sandwich("ayam", "selada", "mayones")
make_sandwich("telur", "saus sambal", "timun", "keju")
