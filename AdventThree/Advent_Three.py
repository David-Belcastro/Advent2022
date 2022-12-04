import string

items = []
sum = 0

priority = 1

priority_list = {}

for letter in string.ascii_letters:
    priority_list[letter] = priority
    priority += 1

pointer = 0

with open('AdventThree/input.txt', 'r') as f:
    lines = f.readlines()
    for x in range(int(len(lines)/3)):
        matched_items = []
        group = x*3
        elf_1 = lines[group]
        elf_2 = lines[group+1]
        elf_3 = lines[group+2]
        for items_1 in elf_1:
            for items_2 in elf_2:
                if items_1 == items_2:
                    matched_items.append(items_1)
        for item in matched_items:
            for items_3 in elf_3:
                if item == items_3:
                    sum += priority_list[item]
                    break
            else: 
                continue
            break

    #     il = int((len(l)-1)/2)
    #     for items_l in l[:il]:
    #         for items_r in l[il:]:
    #             if items_l == items_r:
    #                 sum += priority_list[items_l]
    #                 items.append(items_l)
    #                 break
    #         else:
    #             continue
    #         break
    print(sum)
