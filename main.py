import os
p = input("Principal: ")
r = input("Rate: ")
t = input("Years: ")
p = int(p)
r = float(r)
t = int(t)
amt = 1
tosave = ""
files = []
while amt != t+1:
    p += (p*r)
    print(f"-----\nYear: {amt}\nInterest: {p*r}\nTotal: {p}\n-----\n")
    tosave += f"-----\nYear: {amt}\nInterest: {p*r}\nTotal: {p}\n-----\n"
    amt += 1
for file in os.listdir(os.getcwd()):
    files.append(file)
if "cpdint.txt" not in files:
    os.system(f"touch {os.getcwd()}/cpdint.txt")
with open(f"{os.getcwd()}/cpdint.txt","w") as txt:
    txt.write(tosave)
print("Saved to cpdint.txt!")
