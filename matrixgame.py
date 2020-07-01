from typing import List
def scoreDiff(board: List[List[int]]):
 
  tomScore = 0
  jerryScore = 0
  ncol = len(board[0])
  maxValuesColumn = []
  for c in range(ncol):
    colmn = [row[c] for row in board]
    maxValuesColumn.append(max(colmn))

  tomturn = True
  maxValuesColumn.sort(reverse=True)
 
  for i in range(len(maxValuesColumn)):
    if tomturn == True:
       tomScore += maxValuesColumn[i]
       tomturn = False
    else:
       jerryScore += maxValuesColumn[i]
       tomturn = True

  print(tomScore,jerryScore)


board = [[3,7,5,3,4,5],
        [4,5,2,6,4,5],
        [7,4,9,7,8,3]]
board1 = [[5,7,6,2,8,4,4,8],
          [2,5,4,5,9,8,4,2],
          [5,4,3,9,8,3,3,4],
          [4,9,3,4,6,7,4,9,4],
          [2,4,6,2,9,2,4,2]]
scoreDiff(board)