def printBoard(xstate,zstate):
    zero='X' if xstate[0] else ('O' if zstate[0] else 0)
    one='X' if xstate[1] else ('O' if zstate[1] else 1)
    two='X' if xstate[2] else ('O' if zstate[2] else 2)
    three='X' if xstate[3] else ('O' if zstate[3] else 3)
    four='X' if xstate[4] else ('O' if zstate[4] else 4)
    five='X' if xstate[5] else ('O' if zstate[5] else 5)
    six='X' if xstate[6] else ('O' if zstate[6] else 6)
    seven='X' if xstate[7] else ('O' if zstate[7] else 7)
    eight='X' if xstate[8] else ('O' if zstate[8] else 8)

    print("-------------")
    print(f"| {zero} | {one} | {two} |")
    print(f"| --|---|-- |")
    print(f"| {three} | {four} | {five} |")
    print(f"| --|---|-- |")
    print(f"| {six} | {seven} | {eight} |")
    print("-------------")

def sums(a,b,c):
    return a+b+c
def checkwin(xState,zState):
    wins=[[0,1,2,],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sums(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            printBoard(xState,zState)
            print("'X' Player Won the Match")
            return 1
        if(sums(zState[win[0]],zState[win[1]],zState[win[2]])==3):
            printBoard(xState,zState)
            print("'O' Player Won the Match")
            return 0
        if((xState[0] or zState[0])==1 and (xState[1] or zState[1])==1 and (xState[2] or zState[2])==1 and (xState[3] or zState[3])==1 and (xState[8] or zState[8])==1 and (xState[4] or zState[4])==1 and (xState[5] or zState[5])==1 and (xState[6] or zState[6])==1 and (xState[7] or zState[7])==1 ):
            printBoard(xState,zState)
            print("Game draw 😍")
            break

    return -1
        


if __name__ == "__main__":
    xState=[0,0,0,0,0,0,0,0,0]
    zState=[0,0,0,0,0,0,0,0,0]
    turn=1 # 1 for x and 0 for O


  
    print("Welcome to Manmohan Created tic tac toe Game !")
    while (True):
        printBoard(xState,zState)

        if(turn==1):
            print("'X's chance")
            value=int(input("Enter the 'X' Position in tic tac toe Board: "))
            xState[value]=1
        else:
            print("'O's chance")
            value=int(input("Enter the 'X' Position in tic tac toe Board : "))
            zState[value]=1
        winss=checkwin(xState,zState)
        if(winss!=-1):
            print("GAME OVER 😍")
            break
        turn=1-turn 
  

    