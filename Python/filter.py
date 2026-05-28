seq = [1,2,3,4]

output_filter = filter(lambda x: x**2, seq)
output_map = map(lambda x: x**2, seq)
print(list(output_filter))
print(list(output_map))