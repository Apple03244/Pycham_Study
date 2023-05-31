    def __init__(self,name,age,gender,email):
        self.name=name
        self.age=age
        self.gendef=gender
        self.email=email

    def register(self):
        self.myInfo=self.name+" "+str(self.age)+" "+self.gendef+" "+self.email+" "+str(datetime.now())


