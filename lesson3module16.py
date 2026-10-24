import os
print("==science notes==")
with open("science.txt","r") as f:
    for line in f:
        print(line.strip())

print()

print("==word count==")
with open("maths.txt","r") as f:
    for line in f:
        words=line.split()
        print(len(words),"words->",line.strip())
print()

print("==merging notes==")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists-overwriting")
else:
    print("all-notes.txt not found-creating now")

content = ""
with open("science.txt","r")as f:
    content +="---science.txt--\n"
    content +=f.read() +"\n"
with open("maths.txt","r")as f:
    content +="---maths.txt--\n"
    content +=f.read() +"\n"
with open("all-notes.txt","w")as out:
    out.write(content)
print("saved to all-notes.txt")
print()

if os.path.exists("all-notes.txt"):
    os.remove("all-notes.txt")
    print("all-notes.txt deleted.")
else:
    print("all-notes.txt does not exist.")