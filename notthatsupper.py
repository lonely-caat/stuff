class GenericAnimal(object):
    def __init__(self,name,sound,color,legs,extra=None):
        self.sound=sound
        self.name=name
        self.color=color
        self.legs=legs
        self.extra=extra
    def describer(self):
        print 'This is a {0}, which goes {1}, is very {2}, and walks on {3}'.format(self.name, self.sound, self.color, self.legs)
    def hybrid(self):
        if self.extra:
            self.legs +=  self.extra
        print self.legs

class LikesFood(GenericAnimal):
    def __init__(cls,name,sound,color,legs,food):
            super(LikesFood,cls).__init__(name,sound,color,legs)
            cls.food=food
    def foody(cls):
        return cls.food +'yyyy'
c = LikesFood('Cat','Meow','Black',4,'Whiskas')
print(c.food, c.legs)
print(c.foody())

