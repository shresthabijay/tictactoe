class GameProcess:
    count=0
    def __init__(self):
        GameProcess.count+=1
        self.id=GameProcess.count
        self.game_data=[]
        self.nodes={}
    
    def checkThree(self,data):
        d1=self.dist(data[0],data[1])
        d2=self.dist(data[0],data[2])
        d3=self.dist(data[1],data[2])
        if(d1>d2 and d1<d3):
            l=d1
            s=d2+d3
        elif(d2>d3 and d2>d1):
            l=d2
            s=d1+d3
        else:
            l=d3
            s=d1+d2
        if(l==s):
            return True
        else:
            return False

        
    def checkTwo(self,data):
        if(data[0][0]==data[1][0] or data[0][1]==data[1][1]):
            return True
        elif(data[0][0]==data[0][1] and data[1][0]==data[1][1]):
            return True
        else:
            return False

        


    def dist(self,a,b):
        dist=((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)
        return dist


g1=GameProcess()
print(g1.checkTwo([[0,0],[2,1]]))
    



        
