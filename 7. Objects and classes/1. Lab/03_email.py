class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_list = []
while True:
    command = input()
    if command == "Stop":
        break
    command = command.split()
    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    email_list.append(email)

indices = [int(x) for x in input().split(",")]  #final line, you will be given the indices of the sent emails
for i in indices:
    email_list[i].send()

for element in email_list:
    print(element.get_info())
