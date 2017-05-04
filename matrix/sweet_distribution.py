noOfTestCases = int(raw_input())
def handle_top_left_corner(matrix_size, micro_pos):
  x , y = micro_pos
  n, m = matrix_size
  if(x % 2 == 1):
    if(x == n and y == m):
      return 'Over'
    if(y == m):
      return 'Back'
    else:
      return 'Right'
  elif(x % 2 == 0):
    if(x == n and y == 1):
      return 'Over'
    if(y == 1):
      return 'Back'
    else:
      return 'Left'

def handle_top_right_corner(matrix_size, micro_pos):
  x, y = micro_pos
  n, m = matrix_size
  if(x % 2 == 1):
    if(x == n and y == 1):
      return 'Over'
    if(y == 1):
      return 'Back'
    else:
      return 'Left'
  elif(x % 2 == 0):
    if(x == n  and y == m):
      return 'Over'
    if(y == m):
      return 'Back'
    else:
      return 'Right'

def handle_bottam_left_corner(matrix_size, micro_pos):
  x, y = micro_pos
  n, m = matrix_size
  x = n - x + 1

  if(x % 2 == 1):
    if(x == n and y == m):
      return 'Over'
    if(y == m):
      return 'Front'
    else:
      return 'Right'
  elif(x % 2 == 0):
    if(x == n and y == 1):
      return 'Over'
    if(y == 1):
      return 'Front'
    else:
      return 'Left'


def handle_bottam_right_corner(matrix_size, micro_pos):
  x, y = micro_pos
  n, m = matrix_size
  x = n - x + 1

  if(x % 2 == 1):
    if(x == n and y == 1):
      return 'Over'

    if(y == 1):
      return 'Front'
    else:
      return 'Left'
  elif(x % 2 == 0):
    if(x == n and y == m):
      return 'Over'
    if(y == m):
      return 'Front'
    else:
      return 'Right'



def direction_of_transfer(matrix_size, startPos, micro_pos):
  x, y = startPos
  n, m = matrix_size
  if(x == 1 and y == 1):
    return handle_top_left_corner(matrix_size, micro_pos)
  if(x == 1 and y == m):
    return handle_top_right_corner(matrix_size, micro_pos)
  if(x == n and y == m):
    return handle_bottam_right_corner(matrix_size, micro_pos)
  if(x == n and y == 1):
    return handle_bottam_left_corner(matrix_size, micro_pos)


for _ in range(noOfTestCases):
  matrix_size = map(int, raw_input().split(" "))
  startPos = map(int, raw_input().split(" "))
  micro_pos = map(int, raw_input().split(" "))
  print direction_of_transfer(matrix_size, startPos, micro_pos)

