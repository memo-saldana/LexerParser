

class TokenType:
  INTEGER = 0
  REGISTER = 1
  ASSIGNMENT = 2
  OPERATION = 3
  EOF = 4


class Token:

  def __init__(self, type, value):
    super().__init__()
    self.type = type
    self.value = value

  def __str__(self):
    return self.value
