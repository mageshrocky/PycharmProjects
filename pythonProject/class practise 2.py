class bike:
    def __init__(self,name,engine,top_speed):
        self.name = name
        self.engine = engine
        self.top_speed = top_speed
    def specs(self):
        print('specs:',self.name,self.engine,self.top_speed)

bike1 = bike('pulsar','200cc','150km/hr')
bike1.specs()

bike2 = bike('hornet','160cc','100km/hr')
bike2.specs()
