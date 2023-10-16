text = "FFLPPFLPLNLPTPPPNFPF"
char_list = []
compress = ""

def findList(arr, key):
    for i in range(len(arr)):
        if arr[i][0] == key:
            return i
    return -1

for i in range(len(text)):
    tmp = findList(char_list, text[i])
    if tmp != -1:
        char_list[tmp][1] += 1
    else:
        char_list.append([text[i], 1])

char_list.sort(key = lambda x: x[1], reverse = True)

for i in range(len(text)):
    fnd = findList(char_list, text[i])
    compress += ("0" * fnd) + "1"

print("compressed =", compress)