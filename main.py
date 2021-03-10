from Lexer import Lexer

def main():
  lexer = Lexer()
  test = "MOV 2354 #A MOV #A #C SUM #A #B ;"
  
  tokens = lexer.scan(test)
  print([t.value for t in tokens])

if __name__ == "__main__":
    main()