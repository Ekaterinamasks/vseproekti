#крестики нолики игра
maps = [1,2,3,4,5,6,7,8,9]
 

pobeda = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 

def vivod_karti():
    print(maps[0], end =" ")
    print(maps[1], end =" ")
    print(maps[2])
 
    print(maps[3], end =" ")
    print(maps[4], end =" ")
    print(maps[5])
 
    print(maps[6], end =" ")
    print(maps[7], end =" ")
    print(maps[8])    
 

def hod_v_iacheiky(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 

def tecuschii_rezylt():
    win = ""
 
    for i in pobeda:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "Игрок1"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "Игрок2"   
             
    return win
 
# Основная программа
finish = False
player1 = True
count=9
while finish == False:
    vivod_karti()
 
    # куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("игрок1, жги: "))
        count-=1
    else:
        symbol = "O"
        step = int(input("Игрок2, жги: "))
        count-=1
    hod_v_iacheiky(step,symbol) # ход в ячейку
    win = tecuschii_rezylt() #определение победителя
    if win != "":
        finish = True
        print("ты лучший", win)
    else:
        finish = False
    if count==0:
     print("вот это вы мощные, жесточайший бой , который закончился ничьей, еще боечек?")
     break
 
    player1 = not(player1)        
 
       
vivod_karti()

