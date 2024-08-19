card_no = "5610591081018251"
odd_sum = 0
double_list = []
even_sum = 0
number = list(card_no)

for (idx, val) in enumerate(number):
    #print(str(idx) + '=>' + val)
    if idx %2 != 0:
        odd_sum += int(val)
    else:       #this is an even number
        double_list.append(int(val)*2)

#print(odd_sum)


#converting the list into a string
double_string = ""
for x in double_list:
    double_string += str(x)
#print(double_string)

#converting the string back to a list
double_list = list(double_string)
for x in double_list:
    even_sum += int(x)

net_sum = odd_sum + even_sum
if net_sum % 10 == 0:
    print('Valid card!')
else:
    print('Invalid card!')