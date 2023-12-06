import copy


class Minimax:
    def __init__(self):
        self.evaluationCount = 0
        self.winScore = 100000000
        self.gameOver = False

    def getGameStatus(self):
        return self.gameOver

    def getWinScore(self):
        return self.winScore

    def evaluateBoardForWhite(self, game_state, blacksTurn):
        self.evaluationCount += 1
        blackScore = self.getScore(game_state, True, blacksTurn)
        whiteScore = self.getScore(game_state, False, blacksTurn)
        if blackScore == 0:
            blackScore = 1.0
        return whiteScore / blackScore

    def getScore(self, game_state, forBlack, blacksTurn):
        boardMatrix = copy.deepcopy(game_state)
        score = self.evaluateHorizontal(boardMatrix, forBlack, blacksTurn) + self.evaluateVertical(boardMatrix,
                                                                                                   forBlack,
                                                                                                   blacksTurn) + self.evaluateDiagonalLeft(
            boardMatrix, forBlack, blacksTurn) + self.evaluateDiagonalRight(boardMatrix, forBlack, blacksTurn)
        # print("score --> ", score)
        return score

    def evaluateHorizontal(self, boardMatrix, forBlack, playersTurn):
        consecutive = 0
        blocks = 1
        score = 0
        # print(type(boardMatrix[0][0]))
        for i in range(len(boardMatrix)):
            for j in range(len(boardMatrix[0])):
                # print("in here", i," ", j, " ", boardMatrix[i][j])

                # if boardMatrix[i][j] == (2 if forBlack else 1):
                if boardMatrix[i][j] == ('B' if forBlack else 'W'):
                    consecutive += 1
                # elif boardMatrix[i][j] == 0:
                elif boardMatrix[i][j] == '_':
                    if consecutive > 0:
                        blocks -= 1
                        score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
                        consecutive = 0
                        blocks = 1
                    else:
                        blocks = 1
                elif consecutive > 0:
                    score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
                    consecutive = 0
                    blocks = 2
                else:
                    blocks = 2
                # print("Cell -> ", i+1, " ", j+1)
                # print("Consecutive -> ", consecutive)
                # print("Blocks -> ", blocks, '\n\n\n\n')
            if consecutive > 0:
                score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)

            consecutive = 0
            blocks = 2

        # print("horizontal score -->", score)
        return score

    def evaluateVertical(self, boardMatrix, forBlack, playersTurn):
        consecutive = 0
        # blocks = 2
        blocks = 1
        score = 0

        for j in range(len(boardMatrix[0])):
            for i in range(len(boardMatrix)):
                # if boardMatrix[i][j] == (2 if forBlack else 1):
                if boardMatrix[i][j] == ('B' if forBlack else 'W'):
                    consecutive += 1
                elif boardMatrix[i][j] == '_':
                    if consecutive > 0:
                        blocks -= 1
                        score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
                        consecutive = 0
                        blocks = 1
                    else:
                        blocks = 1
                elif consecutive > 0:
                    score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
                    consecutive = 0
                    blocks = 2
                else:
                    blocks = 2

            if consecutive > 0:
                score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
            consecutive = 0
            blocks = 2

        return score

    def evaluateDiagonalLeft(self, boardMatrix, forBlack, playersTurn):
        consecutive = 0
        blocks = 1
        score = 0

        # for k in range(-len(boardMatrix) + 1, len(boardMatrix)):
        for k in range(0, 2 * (len(boardMatrix) - 1) + 1):
            # iStart = max(0, k)
            iStart = max(0, k - len(boardMatrix) + 1)
            # iEnd = min(len(boardMatrix) + k - 1, len(boardMatrix) - 1)
            iEnd = min(len(boardMatrix) - 1, k)
            for i in range(iStart, iEnd + 1):
                # j = k-i
                j = i - k

                if boardMatrix[i][j] == ('B' if forBlack else 'W'):
                    consecutive += 1
                elif boardMatrix[i][j] == '_':
                    if consecutive > 0:
                        blocks -= 1
                        score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
                        consecutive = 0
                        blocks = 1
                    else:
                        blocks = 1
                elif consecutive > 0:
                    score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
                    consecutive = 0
                    blocks = 2
                else:
                    blocks = 2

            if consecutive > 0:
                score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
            consecutive = 0
            blocks = 2

        return score

    def evaluateDiagonalRight(self, boardMatrix, forBlack, playersTurn):
        consecutive = 0
        blocks = 1
        score = 0

        # for k in range(-len(boardMatrix) + 1, len(boardMatrix)):
        for k in range(0, 2 * (len(boardMatrix) - 1) + 1):
            # iStart = max(0, k)
            iStart = max(0, k - len(boardMatrix) + 1)
            # iEnd = min(len(boardMatrix) + k - 1, len(boardMatrix) - 1)
            iEnd = min(len(boardMatrix) - 1, k)
            for i in range(iStart, iEnd + 1):
                j = k - i
                # j=i-k

                if boardMatrix[i][j] == ('B' if forBlack else 'W'):
                    consecutive += 1
                elif boardMatrix[i][j] == '_':
                    if consecutive > 0:
                        blocks -= 1
                        score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
                        consecutive = 0
                        blocks = 1
                    else:
                        blocks = 1
                elif consecutive > 0:
                    score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
                    consecutive = 0
                    blocks = 2
                else:
                    blocks = 2

            if consecutive > 0:
                score += self.getConsecutiveSetScore(consecutive, blocks, forBlack == playersTurn)
            consecutive = 0
            blocks = 2

        return score

    def getConsecutiveSetScore(self, count, blocks, currentTurn):
        winGuarantee = 1000000
        if blocks == 2 and count < 5:
            return 0

        if count == 5:
            return self.winScore
        elif count == 4:
            if currentTurn:
                return winGuarantee
            else:
                if blocks == 0:
                    return winGuarantee / 4
                else:
                    return 200
        elif count == 3:
            if blocks == 0:
                if currentTurn:
                    return 50000
                else:
                    return 200
            else:
                if currentTurn:
                    return 10
                else:
                    return 5
        elif count == 2:
            if blocks == 0:
                return 7 if currentTurn else 5
            else:
                return 3
        elif count == 1:
            return 1

        return self.winScore * 2

    def calculateNextMove(self, depth, game_state, player_marker):
        move = [None, None]

        bestMove = self.searchWinningMove(game_state, player_marker)
        # bestMove = None
        if bestMove is not None:
            move[0] = bestMove[1]
            move[1] = bestMove[2]
            self.gameOver = True
        else:
            bestMove = self.minimaxSearchAB(depth, game_state, True, -1.0, self.getWinScore(), player_marker)
            if bestMove is None:
                move = None
            else:
                move[0] = bestMove[1]
                move[1] = bestMove[2]

        self.evaluationCount = 0

        return move

    # def calculateNextMove(self, depth):
    #     move = [None, None]
    #
    #     bestMove = self.searchWinningMove(game_state)
    #
    #     if bestMove is not None:
    #         move[0] = bestMove[1]
    #         move[1] = bestMove[2]
    #         self.gameOver = True
    #     else:
    #         bestMove = self.minimaxSearchAB(depth, self.board, True, -1.0, self.getWinScore())
    #         if bestMove is None:
    #             move = None
    #         else:
    #             move[0] = bestMove[1]
    #             move[1] = bestMove[2]
    #
    #     self.evaluationCount = 0
    #
    #     return move

    def minimaxSearchAB(self, depth, game_state, maxPlayer, alpha, beta, player_marker):
        # print("----------in minimax depth----------", depth)
        if depth == 0:
            # lala=[self.evaluateBoardForWhite(game_state, not maxPlayer), None, None]
            lala = [self.evaluateBoardForWhite(game_state, maxPlayer), None, None]
            # print("final move")
            # print(lala)
            return lala

        allPossibleMoves = self.generate_all_adjacent_move(game_state)
        # print(allPossibleMoves)
        # return None;

        if len(allPossibleMoves) == 0:
            return [self.evaluateBoardForWhite(game_state, not maxPlayer), None, None]

        bestMove = [None, None, None]

        if maxPlayer:
            # alpha = -1.0
            bestMove[0] = -1.0;

            for move in allPossibleMoves:
                # from deepcopy import deepcopy, deepdeepcopy
                # dummyBoard = deepdeepcopy(game_state)
                dummyBoard = copy.deepcopy(game_state)
                # if dummyBoard[move[0]][move[1]]!='_':
                #     continue
                dummyBoard[move[0]][move[1]] = 'W'

                # dummyBoard.addStoneNoGUI(move[1], move[0], not maxPlayer)  # Pass the player_marker

                tempMove = self.minimaxSearchAB(depth - 1, dummyBoard, not maxPlayer, alpha, beta, player_marker)
                # print("--------searching moves--------------")
                # print("temp move", tempMove)
                # dummyBoard[move[0]][move[1]] = '_'
                if tempMove[0] > alpha:
                    alpha = tempMove[0]

                if tempMove[0] >= beta:
                    return tempMove

                if tempMove[0] > bestMove[0]:
                    bestMove = tempMove
                    bestMove[1] = move[0]
                    bestMove[2] = move[1]
        else:
            # beta = 100000000.0
            bestMove[0] = 100000000.0
            bestMove[1] = allPossibleMoves[0][0]
            bestMove[2] = allPossibleMoves[0][1]
            for move in allPossibleMoves:
                dummyBoard = copy.deepcopy(game_state)
                # dummyBoard.addStoneNoGUI(move[1], move[0], not maxPlayer)  # Pass the player_marker
                dummyBoard[move[0]][move[1]] = 'B'

                tempMove = self.minimaxSearchAB(depth - 1, dummyBoard, not maxPlayer, alpha, beta, player_marker)

                if tempMove[0] < beta:
                    beta = tempMove[0]

                if tempMove[0] <= alpha:
                    return tempMove

                if tempMove[0] < bestMove[0]:
                    bestMove = tempMove
                    bestMove[1] = move[0]
                    bestMove[2] = move[1]

        return bestMove

    def searchWinningMove(self, game_state, player_marker):
        allPossibleMoves = self.generate_all_adjacent_move(game_state)
        winningMove = [None, None, None]

        for move in allPossibleMoves:
            self.evaluationCount += 1
            dummyBoard = copy.deepcopy(game_state)
            dummyBoard[move[0]][move[1]] = 'W'

            # dummyBoard.addStoneNoGUI(move[1], move[0], player_marker == 'B')  # Pass the player_marker

            if self.getScore(dummyBoard, False, False) >= self.winScore:
                winningMove[1] = move[0]
                winningMove[2] = move[1]
                return winningMove

        return None

    # def searchWinningMove(self, game_state):
    #     allPossibleMoves = self.generate_possible_moves(game_state)
    #     winningMove = [None, None, None]
    #
    #     for move in allPossibleMoves:
    #         self.evaluationCount += 1
    #         dummyBoard = board.clone()
    #         dummyBoard.addStoneNoGUI(move[1], move[0], False)
    #
    #         if self.getScore(dummyBoard, False, False) >= self.winScore:
    #             winningMove[1] = move[0]
    #             winningMove[2] = move[1]
    #             return winningMove
    #
    #     return None

    def generate_possible_moves(self, game_state):
        possible_moves = []
        for row in range(len(game_state)):
            for col in range(len(game_state[0])):
                if game_state[row][col] == "_":
                    possible_moves.append((row, col))
        return possible_moves

    def generate_all_adjacent_move(selfslef, game_sate):
        # print("#-2")
        possible_moves = []

        for row in range(len(game_sate)):
            for col in range(len(game_sate)):
                if game_sate[row][col] == '_':
                    if row != 0 and col != 0 and game_sate[row - 1][col - 1] != "_":
                        possible_moves.append((row, col))
                    elif row != 0 and game_sate[row - 1][col] != "_":
                        possible_moves.append((row, col))
                    elif row != 0 and col != 9 and game_sate[row - 1][col + 1] != "_":
                        possible_moves.append((row, col))
                    elif col != 0 and game_sate[row][col - 1] != "_":
                        possible_moves.append((row, col))
                    elif col != 9 and game_sate[row][col + 1] != "_":
                        possible_moves.append((row, col))
                    elif row != 9 and col != 0 and game_sate[row + 1][col - 1] != "_":
                        possible_moves.append((row, col))
                    elif row != 9 and game_sate[row + 1][col] != "_":
                        possible_moves.append((row, col))
                    elif row != 9 and col != 9 and game_sate[row + 1][col + 1] != "_":
                        possible_moves.append((row, col))
        # print("possible moves: ", possible_moves)
        return possible_moves

    def generateMoves(self, game_state):
        moves = []
        for row in range(len(game_state)):
            for col in range(len(game_state[0])):
                if game_state[row][col] == "_":
                    moves.append((row, col))
        return moves

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

