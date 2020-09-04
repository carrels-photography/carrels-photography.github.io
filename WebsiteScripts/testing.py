line_content = "19-45"

low_up = line_content.split("-")

print(low_up)

for index in range(int(low_up[0]), int(low_up[1]) +1):
    print(index)