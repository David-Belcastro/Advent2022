pairs = 0

with open('AdventFour/Input.txt','r') as f:
    for line in f:
        line = line.rstrip('\n')
        assignments = line.split(',')
        assigment_one = assignments[0].split('-')
        assigment_two = assignments[1].split('-')
        if (int(assigment_one[0]) <= int(assigment_two[0]) and int(assigment_one[1]) >= int(assigment_two[1]))\
        or (int(assigment_one[0]) >= int(assigment_two[0]) and int(assigment_one[1]) <= int(assigment_two[1]))\
        or (int(assigment_two[0]) >= int(assigment_one[0]) and int(assigment_two[0]) <= int(assigment_one[1]))\
        or (int(assigment_two[1]) >= int(assigment_one[0]) and int(assigment_two[1]) <= int(assigment_one[1])):
           
            print([assigment_one,assigment_two,'true'])
            pairs += 1
        else:
            print([assigment_one,assigment_two,'false'])


print(pairs)