def digits_increase(number):
    newnumber=str(number)
    max_digit=int(newnumber[0])

    for digit in newnumber:
        if int(digit) > max_digit:
            max_digit = int(digit)
        elif int(digit) < max_digit:
            return False
    return True


def has_double(number):
    newnumber=str(number)
    for k in range(len(newnumber)-1):
        if newnumber[k]==newnumber[k+1]:
            return True
    return False

def break_down_matching_group(number):
    newnumber = str(number)
    current_digit = newnumber[0]
    digit_groups=[1]
    for k in range(1,len(newnumber)):
        if newnumber[k]==current_digit:
            digit_groups[-1]+=1
        else:
            current_digit = newnumber[k]
            digit_groups += [1]
    return digit_groups



counter=0
for k in range(357253,892942):
    if digits_increase(k) and has_double(k):
        # print(k)
        counter+=1


print(counter)

print(break_down_matching_group(111122))

counter=0
for k in range(357253,892942):
    if digits_increase(k) and (2 in break_down_matching_group(k)):
        # print(k)
        counter+=1

print(counter)
