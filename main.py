from Lexer import Lexer
from Parser import Parser

def main():
  lexer = Lexer()
  test = "MOV 2354 #A MOV #A #C SUM #A #B ;"
  
  tokens = lexer.scan(test)

  print([t.value for t in tokens])

  for token in tokens:
    print ("<" + token.getTypeString() + ", " + token.value + ">")

  parser = Parser()
  parser.parse(tokens)



if __name__ == "__main__":
    main()