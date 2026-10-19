class Notification:
    def send(self):
        print("Sending notification")

class Email(Notification) :
    def send(self):
        print("sending email")
sent = Email()
sent.send()