gameOver = False

player1 = [1,1]

player2 = [1,1]

def status():
    print()
    print('Current Status :')
    print("Player1 : " + str(player1[0]) + " " + str(player1[1]))
    print("Player2 : " + str(player2[0]) + " " + str(player2[1]))
    print()

def whoWon(num):
    print('------------------------------------------------------------')
    print( '           Player' + str(num) + ' WON !!')
    print('------------------------------------------------------------')
    gameOver = True

def splitMove(hand, num1, num2,player):
    if(player == 1):
        player2[0] = num1
        player2[1] = num2
    if(player == 2):
        player1[0] = num1
        player1[1] = num2

    status()

def attackMove(hand1, hand2,player):
    if(player == 1):
        if(hand1 == 'R') :
            if(hand2 == 'R'):
                player2[1] += player1[1]
            elif(hand2 == 'L'):
                player2[0] += player1[1]
        elif(hand1 == 'L'):
            if(hand2 == 'R'):
                player2[1] += player1[0]
            elif(hand2 == 'L'):
                player2[0] += player1[0]
    if(player == 2):
        if(hand1 == 'R') :
            if(hand2 == 'R'):
                player1[1] += player2[1]
            elif(hand2 == 'L'):
                player1[0] += player2[1]
        elif(hand1 == 'L'):
            if(hand2 == 'R'):
                player1[1] += player2[0]
            elif(hand2 == 'L'):
                player1[0] += player2[0]
    
    if(player1[0] >= 5):
        player1[0] = 0
    if(player2[0] >= 5):
        player2[0] = 0
    if(player1[1] >= 5):
        player1[1] = 0
    if(player2[1] >= 5):
        player2[1] = 0

    if (player1[0] == 0 and player1[1] == 0):
        gameOver = True
        whoWon(2)
    
    if (player2[0] == 0 and player2[1] == 0):
        gameOver = True
        whoWon(1)

    status()

status()

while ( gameOver == False ):
    player = 1
    print("Enter move for Player1 : ")
    move = input()

    print("Enter move Combination : ")
    moveCombo = input()

    if (move == 'A'):
        h1,h2 = moveCombo.split()
        attackMove(h1,h2,player)

    if (move == 'S'):
        h,a1,a2 = moveCombo.split()
        splitMove(h,a1,a2,player)

    player = 2
    print("Enter move for Player2 : ")
    move = input()

    print("Enter move Combination : ")
    moveCombo = input()

    if (move == 'A'):
        h1,h2 = moveCombo.split()
        attackMove(h1,h2,player)

    if (move == 'S'):
        h,a1,a2 = moveCombo.split()
        splitMove(h,a1,a2,player)

    