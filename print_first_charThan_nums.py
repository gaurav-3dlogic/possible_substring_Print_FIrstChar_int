#string = "A12B7E8OM"
string = input("Enter a string: ")

char = []
nums = []



for i in string:
    if i.isalpha():
        char.append(i)
    else:
        nums.append(i)
res = sorted(char)+sorted(nums)

print(''.join(res))

        