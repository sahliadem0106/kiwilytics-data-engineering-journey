#list :
list1=[1,2,3,4,5]
print(list1)
#lets slice it 
print(list1[0:3])   # 0 included & the 3 is not   from 0 to 2                                                |
print(list1[1:4:2])    #third parametre is the step of moving                                                |
print(list1[0:])      # 0:  men from the begg to the end0 included kel 3ada                                  |
print(list1[:2])       #:2   men louul lin 2 -1 ( kima 9olna its not included)    : mel extremite             \
print(list1[::2])    #  mel extrimite lel extrimite but with pace = 2 starting from first value                \ 
# u are not gonna know the values always so u need to manage a list of n elements in it not a known number     /
print(list1[-1])    # it wil bring the last element in the list                                               /
#list of lists                                                                                                |
print([list1]*2)                                                                                           #  |
#printing repeated                                                                                            |
print(list1[1:4:2]*2)                                  #<=====================================================
## using data in lists and make operations 
print(2*i for i in list1 )