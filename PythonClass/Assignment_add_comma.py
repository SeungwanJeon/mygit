import math
#과제 2 add comma
def add_comma(val):
    temp_list=[i+3 for i in range(0,round(math.log10(val)),3)]
    val_list=list(str(val))
    val_list.reverse()
    for i in range(len(temp_list)):
        val_list.insert(temp_list[i]+i,',')
    val_list.reverse()
    return ''.join(val_list)

print(add_comma(1234567))
val=1234567

a=list(range(5))
a.reverse()
print(a)
reversed(list(range(5)))
