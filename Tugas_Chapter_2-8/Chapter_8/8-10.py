def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

messages = ["Halo!", "Apa kabar?", "Semangat belajar Python!"]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Daftar asli:", messages)
print("Pesan terkirim:", sent_messages)
