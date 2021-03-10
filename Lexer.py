import sys

from Token import Token, TokenType

class Lexer:
  ERROR = 9999
  transitionMatrix = [
    [0, 1, 3, 2, 104, ERROR],
    [101, 1, ERROR, ERROR, ERROR, ERROR],
    [ERROR, ERROR, 102, ERROR, ERROR, ERROR],
    [103, ERROR, 3, ERROR, ERROR, ERROR]
  ]

  def scan(self, str):
    tokens = []
    strIndex = 0
    while(strIndex < len(str)):
      val = ""
      state = 0
      
      while( state<100 and strIndex<len(str)):
        currentChar = str[strIndex]
        strIndex += 1
        state = self.transitionMatrix[state][self.__charFilter(currentChar)]
        if(state > 0):
          val += currentChar

      val = val.strip()  

      if(state == 0): # end of string with whitespace
        return tokens
      elif(state == 101): # valid integer
        tokens.append(Token(TokenType.INTEGER, val))
      elif(state == 102): # valid register
        if(val in ["#A", "#B", "#C", "#D"]):
          tokens.append(Token(TokenType.REGISTER, val))
        else:
          sys.exit("UNIDENTIFIED TOKEN: " + val + "WHEN CREATING REGISTER TOKEN")
      elif(state == 103):
        if(val in ["SUM", "SUB", "MUL", "DIV"]):
          tokens.append(Token(TokenType.OPERATION, val))
        elif(val == "MOV"):
          tokens.append(Token(TokenType.ASSIGNMENT, val))
        else:
          sys.exit("UNIDENTIFIED TOKEN: \'" + val + "\' WHEN CREATING OPERATION/ASSIGNMENT TOKEN")
      elif(state == 104):
        tokens.append(Token(TokenType.EOF, val))
    
    return tokens



  def __charFilter(self, char):
    if(char == ' ' or char == '\t' or char == '\n'): # ignore whitespace
      return 0
    elif(char >= '0' and char <= '9'): # digits
      return 1
    elif(char >= 'A' and char <= 'Z'): # letter
      return 2
    elif(char == '#'): # register identifier
      return 3
    elif(char == ';'): # eof identifier
      return 4
    else:
      return 5