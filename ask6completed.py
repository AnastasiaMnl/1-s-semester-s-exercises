import random

white = 0
black = 0  
pionia = ["queen","rook","bishop"]
places64 = [] 
board = [] 
for i in range (64):
    places64.append(i) 
    board.append(" ")

places3 = []
for round in range (100): 
    for i in range (len(pionia)):
        a = random.choice(places64) 
        places3.append(a)
        if (board [a] == " ") :
            board [a] = pionia[i] 
    #WHITE
    if (round%2 == 0) :
        if ( abs(places3[0]-places3[1])<8 or ( places3[0]%8 == places3[1]%8 )):
            white += 1
        if ( places3[0]%9 == places3[2] or places3[0]%7 == places3[2]%7 ) :
            white += 1      
    #BLACK
    elif (round%2 == 1) :
        if (abs(places3[0]-places3[1])<8 or( places3[0]%8 == places3[1]%8 )):
            black +=1         
        elif ( places3[0]%9 == places3[1] or places3[0]%7 == places3[1]%7) :
            black +=1   
        if (abs(places3[0]-places3[2])<8 or( places3[0]%8 == places3[2]%8 )):
            black +=1        
        elif ( places3[0]%9 == places3[2] or places3[0]%7 == places3[2]%7) :
            black +=1


print ("WHITE'S SCORE : ", white)
print ("BLACK'S SCORE : ", black)
    