countries = ["India", "Ireland", "Iran", "Cuba", "Australia", "Iceland", "Srilanka", "England"]

counter = 0
output = []
for c in countries:
    if c[0] == "I":
        counter +=1
        output.append(c)
print(counter)
print(output)