'''
게임판이 주어졌을 때 규칙에 맞는 게임판인지 확인하기
주어진 규칙에 맞지 않는 경우는 무엇이 있을까?
  둔 수의 수가 안 맞을 때
    선공이 O이므로 O의 수 - X의 수 = 1 또는 0이어야함.
  승리했는데도 또 두었을 때
    둘 모두 승리한 경우는 존재할 수 없음.
    한쪽이 승리했는데 또 둔 경우가 있을까?
      O가 최소 수로 두어서 이겼는데 X가 또 둔 경우
      O가 이겼다면 O가 한 수 더 많아야함
      같은 이유로 X가 이겼다면 둔 수의 수가 똑같아야함
      
케이스 생각해보기
  OOO  OXO  OOO
  XXO  XOX  .XX
  XXO  OXO  X..
  가능  가능  불가능
  
'''
def solution(board):
    o_count = count(board, 'O')
    x_count = count(board, 'X')
    is_wrong = any([
        not (o_count - x_count == 0 or o_count - x_count == 1),
        is_win(board, 'O') and is_win(board, 'X'),
        is_win(board, 'O') and x_count == o_count,
        is_win(board, 'X') and x_count != o_count,
    ])
    return 0 if is_wrong else 1

def count(board, cell):
    count = 0
    for row in board:
        for c in row:
            if c == cell: count += 1
    return count

def is_win(board, player):
    return any([
        # 가로 승리 조건
        all([cell == player for cell in board[0]]),
        all([cell == player for cell in board[1]]),
        all([cell == player for cell in board[2]]),
        # 세로 승리 조건
        all([row[0] == player for row in board]),
        all([row[1] == player for row in board]),
        all([row[2] == player for row in board]),
        # 대각 승리 조건
        board[0][0] == board[1][1] == board[2][2] == player,
        board[0][2] == board[1][1] == board[2][0] == player,
    ])
