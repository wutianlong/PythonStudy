abc = range(6)

print abc

test_list = [1,2,3,4,5,6,7,8,9]

for i in test_list:
    if i %2 ==0:
        continue;
    else:
        print i;



def square_number(a):
    a[0]= -1;
    return;

#print test_list
print square_number(test_list)

print test_list

class Bird(object):
    yumao = 'yumao'
    age =10;

    def move(self,x,y):
        position = [1,2]
        position[0]= position[0]+x
        position[1]= position[1]+y
        print self.yumao
        return position

bird =Bird();
print bird.yumao
print bird.age
print bird.move(1,2)
