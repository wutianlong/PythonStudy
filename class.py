class Bird(object):
#    def __init__(self):
#        print 'default init method'

    classvalue = 1

    def __init__(self,gender_var):
        self.gender = gender_var
        self.classvalue =2
        print 'invoki __init__ method ,var =',gender_var

    def getClassValue(self):
        print 'value ===',self.classvalue

bird = Bird('girl')
print bird.gender

#print bird.classvalue
bird.getClassValue()
print dir(bird)
