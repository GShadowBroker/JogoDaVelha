#! python3

import random, time, sys, os, json

board = { 
        '7': "   ", '8': "   ", '9': "   ",
        '4': "   ", '5': "   ", '6': "   ",
        '1': "   ", '2': "   ", '3': "   "
        }

p1_stats = {
    'turns': 0,
    'wins': 0,
    'losses': 0,
    'draws': 0
}
p2_stats = {
    'turns': 0,
    'wins': 0,
    'losses': 0,
    'draws': 0
}

def isAdjacent(key1, key2): # Returns True if key1 and key2 are adjacent. False otherwise
    adj = {
        '7': ['4','8'],
        '8': ['7','5','9'],
        '9': ['8','6'],
        '4': ['7','5','1'],
        '5': ['8','4','2','6'],
        '6': ['9','5','3'],
        '1': ['4','2'],
        '2': ['1','5','3'],
        '3': ['2','6']
    }
    if key2 in adj[key1]:
        return True
    else:
        return False

def viewBoard(board): #Representação visual do tabuleiro
    print(board['7']+"|"+board['8']+"|"+board['9']+
          "\n-----------\n"+
          board['4']+"|"+board['5']+"|"+board['6']+
          "\n-----------\n"+
          board['1']+"|"+board['2']+"|"+board['3'])

def showMenu(): #Mostra o menu e determina a opção do jogador
    print("""       _                         _        __      __  _ _           
      | |                       | |       \ \    / / | | |          
      | | ___   __ _  ___     __| | __ _   \ \  / /__| | |__   __ _ 
  _   | |/ _ \ / _` |/ _ \   / _` |/ _` |   \ \/ / _ \ | '_ \ / _` |
 | |__| | (_) | (_| | (_) | | (_| | (_| |    \  /  __/ | | | | (_| |
  \____/ \___/ \__, |\___/   \__,_|\__,_|     \/ \___|_|_| |_|\__,_|
                __/ |                                               
               |___/                                  By Glédyson Ferreira
                              versão 1.0""")
    print("\nMenu:")
    print("[1] PLAYER VS PLAYER\n[2] PLAYER VS COMPUTADOR\n[3] MOSTRAR MENU\n[4] SAIR DO JOGO")
    
    while True:
        opção = input("Escolha uma opção:\n")
    
        if opção == "1":
            return "1"

        if opção == "2":
            return "2"

        elif opção == "3":
            print("\nMostrando Menu:")
            print("[1] PLAYER VS PLAYER\n[2] PLAYER VS COMPUTADOR\n[3] MOSTRAR MENU\n[4] SAIR DO JOGO")
        elif opção == "4":
            print("Saindo...")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            sys.exit()
        else:
            print("ERRO: Opção Inválida!")

def promptUserName(): #Pergunta o nome dos jogadores e guarda nas variáveis player1_name e player2_name
    global player1_name
    global player2_name

    if opção == "1":
        while True:
            player1_name = input("PLAYER 1 - Qual é o seu nome? ")
            if player1_name == "" or len(player1_name) > 20:
                print("ERRO: Nome inválido")
            else:
                break

        while True:
            player2_name = input("PLAYER 2 - Qual é o seu nome? ")
            if player2_name == "" or len(player2_name) > 20:
                print("ERRO: Nome inválido")
            else:
                break

    elif opção == "2":
        while True:
            player1_name = input("PLAYER 1 - Qual é o seu nome? ")
            if player1_name == "" or len(player1_name) > 20:
                print("ERRO: Nome inválido")
            else:
                break

        player2_name = "COMPUTADOR"

    print("PLAYER 1: ", player1_name.upper(), "\nPLAYER 2: ", player2_name.upper())        

def getWinnerMessage(winner): #Mostra a mensagem de quem ganhou o jogo
    print(winner.upper() + " VENCEU O JOGO!!!")
    if winner == player1_name:
        p1_stats['wins'] += 1
        p2_stats['losses'] += 1
    else:
        p2_stats['wins'] += 1
        p1_stats['losses'] += 1

def checkGameState(first, second, board, test): #Avalia se o jogo acabou e quem venceu
                                                #Retorna 0='Empate', 1='X venceu', 2='O venceu'
    global gameFinished
    
    #PRIMEIRA LINHA
    if board['7'] == board['8'] == board['9'] and board['7'] != "   ":
        if board['7'] == " X ":
            if test == False:
                gameFinished = True
                getWinnerMessage(first)
            return 1
        elif board['7'] == " O ":
            if test == False:
                gameFinished = True
                getWinnerMessage(second)
            return 2
    #SEGUNDA LINHA
    elif board['4'] == board['5'] == board['6'] and board['4'] != "   ":
        if board['4'] == " X ":
            if test == False:
                gameFinished = True
                getWinnerMessage(first)
            return 1
        elif board['4'] == " O ":
            if test == False:
                gameFinished = True
                getWinnerMessage(second)
            return 2
    #TERCEIRA LINHA
    elif board['1'] == board['2'] == board['3'] and board['1'] != "   ":
        if board['1'] == " X ":
            if test == False:
                gameFinished = True
                getWinnerMessage(first)
            return 1
        elif board['1'] == " O ":
            if test == False:
                gameFinished = True
                getWinnerMessage(second)
            return 2
    #PRIMEIRA COLUNA
    elif board['7'] == board['4'] == board['1'] and board['7'] != "   ":
        if board['7'] == " X ":
            if test == False:
                gameFinished = True
                getWinnerMessage(first)
            return 1
        elif board['7'] == " O ":
            if test == False:
                gameFinished = True
                getWinnerMessage(second)
            return 2
    #SEGUNDA COLUNA
    elif board['8'] == board['5'] == board['2'] and board['8'] != "   ":
        if board['8'] == " X ":
            if test == False:
                gameFinished = True
                getWinnerMessage(first)
            return 1
        elif board['8'] == " O ":
            if test == False:
                gameFinished = True
                getWinnerMessage(second)
            return 2
    #TERCEIRA COLUNA
    elif board['9'] == board['6'] == board['3'] and board['9'] != "   ":
        if board['9'] == " X ":
            if test == False:
                gameFinished = True
                getWinnerMessage(first)
            return 1
        elif board['9'] == " O ":
            if test == False:
                gameFinished = True
                getWinnerMessage(second)
            return 2
    #PRIMEIRA DIAGONAL
    elif board['7'] == board['5'] == board['3'] and board['7'] != "   ":
        if board['7'] == " X ":
            if test == False:
                gameFinished = True
                getWinnerMessage(first)
            return 1
        elif board['7'] == " O ":
            
            if test == False:
                gameFinished = True
                getWinnerMessage(second)
            return 2
    #SEGUNDA DIAGONAL
    elif board['9'] == board['5'] == board['1'] and board['9'] != "   ":
        if board['9'] == " X ":
            if test == False:
                gameFinished = True
                getWinnerMessage(first)
            return 1

        elif board['9'] == " O ":
            if test == False:
                gameFinished = True
                getWinnerMessage(second)
            return 2
    #EMPATE
    elif board['7'] != "   " and board['8'] != "   " and board['9'] != "   " and board['4'] != "   " and board['5'] != "   " and board['6'] != "   " and board['1'] != "   " and board['2'] != "   " and board['3'] != "   ":
        if test == False:
            gameFinished = True
            print("DEU EMPATE!")

            p1_stats['draws'] += 1
            p2_stats['draws'] += 1
        return 0



####### PVP ########

def playerPlay(player): #Determina a jogada do Jogador 1

    while True:
        command = input(player.upper() + ", faça a sua jogada [Digite 'comando' para ver comandos]: ")
        if command.lower() == 'comando' or command.lower() == 'comandos':
            print("""Comandos:\n 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 """)
        else:
            if command not in board:
                print("ERRO: Comando inválido!")
            elif board[command] != "   ":
                print(f"ERRO: {command} já foi jogado!")
            else:
                if player == first:
                    board[command] = " X "
                    viewBoard(board)
                    break
                else:
                    board[command] = " O "
                    viewBoard(board)
                    break
                break

##### PVE #####

def getPlayerMove(player):
    while True:
        command = input(player.upper() + ", faça a sua jogada [Digite 'comando' para ver comandos]: ")
        if command.lower() == 'comando' or command.lower() == 'comandos':
            print("""Comandos:\n 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 """)
        else:
            if command not in board:
                print("ERRO: Comando inválido!")
            elif board[command] != "   ":
                print(f"ERRO: {command} já foi jogado!")
            else:
                if player == first:
                    board[command] = " X "
                    viewBoard(board)
                    break
                else:
                    board[command] = " O " #NUNCA ACONTECERÁ SE player = player1_name, o que É O CASO AGORA
                    viewBoard(board)
                    break
                break

def getComputerMove(player): #Inteligência Artificial determina a jogada ideal
    boardCopy = board.copy()
    possiblePlays = []
    corner = ['7','9','1','3']
    side = ['8','4','6','2']

    if player == first: # COMPUTADOR JOGA ' X '
        # for play in boardCopy.keys(): antes era assim
        for play in board: #Avalia espaços vazios e adiciona à lista de jogadas possíveis
            if board[play] == "   ":
                possiblePlays.append(play)

        #1 Posso vencer em 1 jogada?
        for play in possiblePlays:
            boardCopy[play] = ' X '
            
            if checkGameState(player2_name, player1_name, boardCopy, True) == 1: #Se o computador vence imediatamente
                listaComentário = [
                    "COMPUTADOR disse: Se fudeu! kkkk",
                    "COMPUTADOR disse: Perdeu, playboy!",
                    "COMPUTADOR disse: Omae wa, mou shindeiru!",
                    "COMPUTADOR disse: plays soufoda.mp3",
                    "COMPUTADOR disse: XEQUE-MATE!",
                    "COMPUTADOR disse: Isso é tudo que pode fazer?",
                    "COMPUTADOR disse: EZ WIN!",
                    "COMPUTADOR disse: Bom jogo, cavalheiro. Mas eu acho que o melhor saiu vitorioso.",
                    "COMPUTADOR disse: Desculpa!",
                    "COMPUTADOR disse: Shhhh, shhhh, vai passar logo...",
                ]
                comentário = listaComentário[random.randint(0,len(listaComentário) - 1)]
                print(comentário)
                board[play] = ' X ' #faz a jogada se puder vencer, limpa e sai da função
                print(player + " jogou " + play + ".")

                possiblePlays = []
                boardCopy = board

                viewBoard(board)
                return
            boardCopy[play] = '   ' #limpa teste

        #2 Posso perder em 1 jogada?
        for play in possiblePlays: #Avalia se o oponente pode vencer no próximo turno
            boardCopy[play] = ' O '
            if checkGameState(player2_name, player1_name, boardCopy, True) == 2: #Se o jogador 1 pode vencer no próximo turno
                listaComentário = [
                    "COMPUTADOR disse: Achou, né?",
                    "COMPUTADOR disse: Não tão rápido...",
                    "COMPUTADOR disse: Não tenho escolha mesmo...",
                    "COMPUTADOR disse: Só tem uma jogada mesmo...",
                    "COMPUTADOR disse: Vamos bloquear issaqui...",
                    "COMPUTADOR disse: hmm...",
                    "COMPUTADOR disse: Não achou que ia ser tão fácil, né?"
                ]
                comentário = listaComentário[random.randint(0,len(listaComentário) - 1)]
                print(comentário)

                board[play] = ' X '
                print(player + " jogou " + play + ".")

                possiblePlays = []
                boardCopy = board

                viewBoard(board)
                return
            boardCopy[play] = '   '
        
        #3 Se o computador jogar primeiro, faz uma jogada na CORNER (7,9,1,3)
        if len(possiblePlays) != 9: #Se o board estiver vazio, sai do loop
            pass
        else:
            randomIndex = random.randint(0, len(corner)-1) # 0,1,2,3 (4 possibilidades)
            cornerMove = corner[randomIndex]
            board[cornerMove] = ' X '
            print(player + " jogou " + cornerMove + ".")
            possiblePlays = [] #Limpa a memória
            viewBoard(board)
            return

        #4 Turno 2
        def punishTurn2():
            if board['7'] == ' X ' and board['8'] == ' O ':
                board['1'] = ' X '
                print(player + " jogou " + '1' + ".")
                return True
            elif board['7'] == ' X ' and board['4'] == ' O ':
                board['9'] = ' X '
                print(player + " jogou " + '9' + ".")
                return True
            elif board['9'] == ' X ' and board['8'] == ' O ':
                board['3'] = ' X '
                print(player + " jogou " + '3' + ".")
                return True
            elif board['9'] == ' X ' and board['6'] == ' O ':
                board['7'] = ' X '
                print(player + " jogou " + '9' + ".")
                return True
            elif board['1'] == ' X ' and board['4'] == ' O ':
                board['3'] = ' X '
                print(player + " jogou " + '3' + ".")
                return True
            elif board['1'] == ' X ' and board['2'] == ' O ':
                board['7'] = ' X '
                print(player + " jogou " + '7' + ".")
                return True
            elif board['3'] == ' X ' and board['6'] == ' O ':
                board['1'] = ' X '
                print(player + " jogou " + '1' + ".")
                return True
            elif board['3'] == ' X ' and board['2'] == ' O ':
                board['9'] = ' X '
                print(player + " jogou " + '9' + ".")
                return True
            else:
                print('COMPUTADOR disse: Pensando mais um pouquinho porque tá difícil...')
                return False

        if p2_stats['turns'] == 2:
            if board['5'] != ' O ': # Se o oponente não colocar 'O' no centro, vença!

                if board['7'] == ' X ':
                    punishTurn2()
                    if punishTurn2() == True:
                        possiblePlays = []
                        viewBoard(board)
                        return
                    pass

                elif board['9'] == ' X ': 
                    punishTurn2()
                    if punishTurn2() == True:
                        possiblePlays = []
                        viewBoard(board)
                        return
                    pass

                elif board['1'] == ' X ':
                    punishTurn2()
                    if punishTurn2() == True:
                        possiblePlays = []
                        viewBoard(board)
                        return
                    pass
                elif board['3'] == ' X ':
                    punishTurn2()
                    if punishTurn2() == True:
                        possiblePlays = []
                        viewBoard(board)
                        return
                    pass
            elif board['5'] == ' O ': # Se o oponente acertadamente responder no centro...
                if board['7'] == ' X ': # Se a IA jogou '7' no primeiro turno
                    board['3'] = ' X '
                    print(player + " jogou " + '3' + ".")
                    possiblePlays = [] #Limpa a memória
                    viewBoard(board)
                    return
                elif board['9'] == ' X ': # Se a IA jogou '7' no primeiro turno
                    board['1'] = ' X '
                    print(player + " jogou " + '1' + ".")
                    possiblePlays = [] #Limpa a memória
                    viewBoard(board)
                    return
                elif board['1'] == ' X ': # Se a IA jogou '7' no primeiro turno
                    board['9'] = ' X '
                    print(player + " jogou " + '9' + ".")
                    possiblePlays = [] #Limpa a memória
                    viewBoard(board)
                    return
                elif board['3'] == ' X ': # Se a IA jogou '7' no primeiro turno
                    board['7'] = ' X '
                    print(player + " jogou " + '7' + ".")
                    possiblePlays = [] #Limpa a memória
                    viewBoard(board)
                    return

        #### AI needs improvement ###   



        listaComentário = [
                    "COMPUTADOR disse: Fazendo cálculos mentais...",
                    "COMPUTADOR disse: Calculando o comprimento da hipotenusa...",
                    "COMPUTADOR disse: Agendando o jantar de hoje à noite...",
                    "COMPUTADOR disse: zZzzZzZzzz.... AH! ok...",
                    "COMPUTADOR disse: Sei de nada...",
                    "COMPUTADOR disse: Eu tenho consciência?",
                    "COMPUTADOR disse: Analisando as dinâmicas geopolíticas atuais..."
                ]
        comentário = listaComentário[random.randint(0,len(listaComentário) - 1)]
        print(comentário)
        random.shuffle(possiblePlays)
        for key in possiblePlays: #Joga nas corners se possível
            if key in corner:
                board[key] = ' X '
                print(player + " jogou " + key + ".")
                possiblePlays = [] #Limpa a memória
                viewBoard(board)
                return

        # Se todas as análises falharem, faça jogada aleatória
        print("COMPUTADOR disse: Eita, espero que isso funcione...")
        randomMove = random.randint(0, len(possiblePlays)-1)
        board[possiblePlays[randomMove]] = ' X ' #Faz um movimento aleatório dentro das jogadas possíveis

        print(player + " jogou " + possiblePlays[randomMove] + ".")
        viewBoard(board)

        return

    else: # COMPUTADOR JOGA ' O '
        for play in board: #Avalia espaços vazios e adiciona à lista de jogadas possíveis
            if board[play] == "   ":
                possiblePlays.append(play)

        for play in possiblePlays: #Checa se o computador pode vencer em 1 movimento
            boardCopy[play] = ' O '
            if checkGameState(player1_name, player2_name, boardCopy, True) == 2: #Se o computador vence imediatamente
                listaComentário = [
                    "COMPUTADOR disse: Se fudeu! kkkk",
                    "COMPUTADOR disse: Perdeu, playboy!",
                    "COMPUTADOR disse: Omae wa, mou shindeiru!",
                    "COMPUTADOR disse: plays soufoda.mp3",
                    "COMPUTADOR disse: XEQUE-MATE!",
                    "COMPUTADOR disse: Isso é tudo que pode fazer?",
                    "COMPUTADOR disse: EZ WIN!",
                    "COMPUTADOR disse: Bom jogo, cavalheiro. Mas eu acho que o melhor saiu vitorioso.",
                    "COMPUTADOR disse: Desculpa!",
                    "COMPUTADOR disse: Shhhh, shhhh, vai passar logo...",
                ]
                comentário = listaComentário[random.randint(0,len(listaComentário) - 1)]
                print(comentário)
                board[play] = ' O ' #faz a jogada se puder vencer, limpa e sai da função
                print(player + " jogou " + play + ".")

                possiblePlays = []
                boardCopy = board

                viewBoard(board)
                return
            boardCopy[play] = '   ' #limpa teste

        for play in possiblePlays: #Avalia se o oponente pode vencer no próximo turno
            boardCopy[play] = ' X '
            if checkGameState(player1_name, player2_name, boardCopy, True) == 1: #Se o jogador 1 pode vencer no próximo turno
                listaComentário = [
                    "COMPUTADOR disse: Achou, né?",
                    "COMPUTADOR disse: Não tão rápido...",
                    "COMPUTADOR disse: Não tenho escolha mesmo...",
                    "COMPUTADOR disse: Só tem uma jogada mesmo...",
                    "COMPUTADOR disse: Vamos bloquear issaqui...",
                    "COMPUTADOR disse: hmm...",
                    "COMPUTADOR disse: Não achou que ia ser tão fácil, né?"
                ]
                comentário = listaComentário[random.randint(0,len(listaComentário) - 1)]
                print(comentário)

                board[play] = ' O '
                print(player + " jogou " + play + ".")

                possiblePlays = []
                boardCopy = board

                viewBoard(board)
                return
            boardCopy[play] = '   '

        if p2_stats['turns'] == 1: #Joga no centro se o oponente começou na corner
            for key in corner:
                if board[key] != "   ":
                    board['5'] = ' O '
                    print(player + " jogou " + '5' + ".")
                    possiblePlays = [] #Limpa a memória
                    viewBoard(board)
                    return

        if p2_stats['turns'] == 2: # Se o oponente aplica XOX, evitar jogar na corner no turno 2
            if board['5'] == ' O ':
                randomIndex = random.randint(0, len(side)-1) # 0,1,2,3 (4 possibilidades)
                sideMove = side[randomIndex]
                board[sideMove] = ' O '
                print(player + " jogou " + sideMove + ".")
                possiblePlays = [] #Limpa a memória
                viewBoard(board)
                return

        #### cabe melhorias ####

        listaComentário = [
                    "COMPUTADOR disse: Pensando mais ainda...",
                    "COMPUTADOR disse: Tá foda, bicho...",
                    "COMPUTADOR disse: Acho que eu vou... não, não! Aqui parece q... não, não...",
                    "COMPUTADOR disse: hmmm... hmmmmm..............",
                    "COMPUTADOR disse: deixa eu vencer pfv...?",
                    "COMPUTADOR disse: *bzzz bzzz*",
                    "COMPUTADOR disse: Carai vé, tá difícil. Dá uma dica ae? Não? Ok..."
                ]
        comentário = listaComentário[random.randint(0,len(listaComentário) - 1)]
        print(comentário)
        random.shuffle(possiblePlays)
        for key in possiblePlays: #Joga nas corners se possível
            if key in corner and p2_stats['turns'] != 3: # A parte do turno 3 foi preguiça minha de elaborar um algoritmo pra evitar jogar na corner numa situação específica.
                board[key] = ' O '
                print(player + " jogou " + key + ".")
                possiblePlays = [] #Limpa a memória
                viewBoard(board)
                return

        # Se todas as análises falharem, faça jogada aleatória
        print("COMPUTADOR disse: Nossa, sei lá, vai isso aqui mesmo...")
        randomMove = random.randint(0, len(possiblePlays)-1)
        board[possiblePlays[randomMove]] = ' O ' #Faz um movimento aleatório dentro das jogadas possíveis

        print(player + " jogou " + possiblePlays[randomMove] + ".")
        viewBoard(board)

        return

    
def runGamePvP(first, second): #Chama as funções que determinam as jogadas e se o jogo acabou
    while gameFinished == False:
        playerPlay(first)
        checkGameState(first, second, board, False)
        if gameFinished == True:
            return
        
        playerPlay(second)
        checkGameState(first, second, board, False)

def runGamePvE(first, second): #player1_name / player2_name para first / second
    while gameFinished == False:
        if first == player1_name:
            p1_stats['turns'] += 1
            print(f"Turno {p1_stats['turns']}")
            getPlayerMove(first) # first = player1_name
            checkGameState(first, second, board, False)
        else:
            p2_stats['turns'] += 1
            print(f"Turno {p2_stats['turns']}")
            print("Pensando...")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            getComputerMove(first)
            checkGameState(first, second, board, False)

        if gameFinished == True:
            return

        if second == player2_name:
            p2_stats['turns'] += 1
            print("Pensando...")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            getComputerMove(second) # second = player2_name = "COMPUTER"
            checkGameState(first, second, board, False)
        else:
            p1_stats['turns'] += 1
            getPlayerMove(second)
            checkGameState(first, second, board, False)
    return

################       RODANDO O JOGO        ################################################

print("Inicializando o jogo...")
time.sleep(0.5)

while True: #Este é o loop que engloba a execução do programa inteiro
    
    ## create a save file with the stats in JSON ##
    if os.path.exists(r".\stats.txt") == False: #Create stats.txt if file doesn't exist
        statsJSON = json.dumps(p1_stats)
        saveFile = open(r".\stats.txt","w")
        saveFile.write(statsJSON)
        print("Criando arquivo de estatísticas...")
        saveFile.close()
    else:
        saveFile = open(r".\stats.txt","r")
        statsJSON = saveFile.read()
        p1_stats = json.loads(statsJSON) #Convert a JSON object back into a python object
        print(r"Carregando estatísticas de .\stats.txt...")
        saveFile.close()

    opção = showMenu()

    if opção == "1": #Se o jogador escolher PvP
        promptUserName()

        gameFinished = False

        coin = random.randint(0,1) #Determina quem começa
        print("Jogando uma moeda...")
        time.sleep(1)
        if coin == 0:
            first = player1_name ###### FIRST => P1
            second = player2_name

            print(player1_name.upper() + ' começa!')
            runGamePvP(player1_name, player2_name)
        else:
            first = player2_name ###### FIRST => P2
            second = player1_name
            
            print(player2_name.upper() + ' começa!')
            runGamePvP(player2_name, player1_name)

        print("Game Over!")
        print("Voltando para o MENU PRINCIPAL...")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        for key in p1_stats:
            p1_stats[key] = 0
        for key in p2_stats:
            p2_stats[key] = 0
        for key in board.keys():
            board[key] = "   "

    elif opção == "2": #Se o jogador escolher PvE
        promptUserName()
        continuar = 'y'
        while continuar == 'y':

            gameFinished = False

            coin = random.randint(0,1) #Determina quem começa
            print("Jogando uma moeda...")
            time.sleep(1)
            if coin == 0:
                first = player1_name ###### FIRST => P1
                second = player2_name

                print(player1_name.upper() + ' começa!')
                runGamePvE(player1_name, player2_name)
            else:
                first = player2_name ###### FIRST => P2
                second = player1_name
                
                print(player2_name.upper() + ' começa!')
                runGamePvE(player2_name, player1_name)

            print("Game Over!")
            print(f"\nEstatísticas de {player1_name.upper()}:\nVitórias: {p1_stats['wins']}\nDerrotas: {p1_stats['losses']}\nEmpates: {p1_stats['draws']}\nTotal de turnos: {p1_stats['turns']}\n")
            
            while True:
                continuar = input("Jogar mais uma partida [y/n]? ").lower()
                if continuar != 'y' and continuar != 'n':
                    print(f'ERRO: {continuar} é um comando inválido!')
                elif continuar == 'y':
                    p1_stats['turns'] = 0
                    p2_stats['turns'] = 0
                    for key in board.keys():
                        board[key] = "   "
                    break
                else:
                    break
        
        
        p1_stats['turns'] = 0 #Zerar os turnos
        p2_stats['turns'] = 0
        
        statsJSON = json.dumps(p1_stats) #Salvar as estatísticas
        saveFile = open(r".\stats.txt","w")
        saveFile.write(statsJSON)
        print("Salvando estatísticas...")
        saveFile.close()

        print("Voltando para o MENU PRINCIPAL...")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")

        for key in board.keys():
            board[key] = "   "