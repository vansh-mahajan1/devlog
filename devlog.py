from datetime import date
topic=input("what have you studied today:")
minutes=int(input("how many minutes does you studied/;"))
time=date.today()
with open("log.txt", "a") as f:
    f.write(f"{time} | {topic} | {minutes}\n")
with open("log.txt","r") as f :
    content=f.read()
print(content)

total = 0

for line in content.split("\n"):
    if line.strip() == "":
        continue
    parts = line.split("|")
    total = total + int(parts[2])

print("Total minutes:", total)