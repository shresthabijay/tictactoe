 
class board:
    count=0
    def __init__(self):
        self.array=[[1,2,3],
                    [4,5,6],
                    [7,8,9]
                    ]
        board.count+=1
        self.id=board.count+1
    
    def display(self):
        print("\n")
        for x in range(0,3,1):
            for y in range(0,3,1):
                print(self.array[x][y],end='')
                print("      ",end='')
            print("\n\n")

    def setPos(self,pos,char):
        self.array[pos[0]][pos[1]]=char
    
    def getPos(self,ind):
        for x in range(0,3,1):
            for y in range(0,3,1):
                if(self.array[x][y]==ind):
                    return [x,y]
       

b1=board()
b1.display()
b1.setPos(b1.getPos(5),'x')
b1.display()