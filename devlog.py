from datetime import date
def germinate():    
    while True:
        try:
            minutes = int(input("How many minutes? "))
            return minutes
        except ValueError:
            print("Please type a number, like 45.")
def get_topic():
    while True:
        topic = input("What have you studied today? ")
        if topic.strip() == "":
            print("Please enter a valid topic.")
        else:
            return topic.strip()
def save_entry(time, topic, minutes):
    with open("log.txt", "a") as f:
        f.write(f"{time} | {topic} | {minutes}\n")
def total_minutes():
    total = 0
    with open("log.txt", "r") as f:
        content = f.read()
    for line in content.split("\n"):
        if line.strip() == "":
            continue
        parts = line.split("|")
        total += int(parts[2])
    return total
def read_log():
    with open("log.txt", "r") as f:
        content = f.read()
    print(content)      

time = date.today()
topic = get_topic()
minutes = germinate()
read_log()
save_entry(time, topic, minutes)
print("Total minutes:", total_minutes())