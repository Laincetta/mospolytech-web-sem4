lines = []
vzrosly = []
pensioner = []
child = []
with open('products.csv', 'r' , encoding="utf-8") as file:
    for word in file.read().splitlines():
        lines.append(word)
for i in range(1,len(lines)):
    vzrosly.append(float(lines[i].split(",")[1]))
    pensioner.append(float(lines[i].split(",")[2]))
    child.append(float(lines[i].split(",")[3]))

print("{:.2f} {:.2f} {:.2f}".format(sum(vzrosly), sum(pensioner), sum(child)))
