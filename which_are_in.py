first_sequence = input().split(', ')
second_sequence = input().split(', ')
substrings = []

for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)

----------------------------------------------

first_sequence = input().split(', ')
second_sequence = input().split(', ')

print([first_string for first_string in first_sequence \
       if any(first_string in second_string for second_string in second_sequence)])

# input -
# arp, live, strong
# lively, alive, harp, sharp, armstrong
#
# output ['arp', 'live', 'strong']
