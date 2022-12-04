from heapq import heappush, nlargest

max_sum = 0
sum_two = 0
sum_three = 0
elf_totals = list()
h = []

with open('AdventOne/input.txt') as f:
        read_data = f.read()
        read_data = str(read_data).split('\n\n')
        read_data.pop()
        for elf in read_data:
            elf_load = list(map(int,elf.split('\n')))
            current_sum = sum(elf_load)
            heappush(h, current_sum)
            if current_sum > max_sum:
                sum_three = sum_two
                sum_two = max_sum
                max_sum = current_sum
            elif current_sum > sum_two:
                sum_three = sum_two
                sum_two = current_sum
            elif current_sum > sum_three:
                sum_three = current_sum
            elf_totals.append(current_sum)
        

elf_totals.sort(reverse=True)
print (sum(nlargest(3,h)))
print(max_sum+sum_two+sum_three)
print(sum(elf_totals[:3]))


