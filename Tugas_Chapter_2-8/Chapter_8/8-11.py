def send_messages(messages, sent_messages):
    while messages:
        sent_messages.append(messages.pop())

messages = ["Halo!", "Apa kabar?", "Semangat belajar Python!"]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Daftar pesan asli:", messages)
print("Pesan arsip:", sent_messages)
