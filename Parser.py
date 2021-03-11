import sys
from Token import Token, TokenType

class Parser:

    def __init__(self, ):
        super().__init__()

    def match(self, tokens, expectedToken):
        if ( (not len(tokens) == 0) and tokens[0].equalsToken(expectedToken)):
            del tokens[0]
            return True
        else:
            if (len(tokens) == 0):
                print("ERROR: Expecting " + expectedToken.value + ", found nothing")
            else:
                print("ERROR: Expecting " + expectedToken.value + ", found " + tokens[0].value)
            print("stopping program")
            sys.exit() 
            return False

    def parse(self, tokens):
        self.parseAux(tokens)
        print("Well formed expression")

    def parseAux(self, tokens):
        if (len(tokens) == 0):
            print("SYNTACTIC ERROR: Expecting a token, found nothing")
            print("Ending program")
            sys.exit()
        elif tokens[0].getType() == TokenType.EOF:
            self.match(tokens, Token(TokenType.EOF, ";"))
            return

        elif (tokens[0].getType() == TokenType.OPERATION):
            self.match(tokens, Token(TokenType.OPERATION, ""))
            self.match(tokens, Token(TokenType.REGISTER, ""))
        elif (tokens[0].getType() == TokenType.ASSIGNMENT):
            self.match(tokens, Token(TokenType.ASSIGNMENT, "MOV"))
            if (tokens[0].getType() == TokenType.REGISTER):
                self.match(tokens, Token(TokenType.REGISTER, ""))
            elif (tokens[0].getType() == TokenType.INTEGER):
                self.match(tokens, Token(TokenType.INTEGER, ""))
        else:
            print("ERROR: Unexpected \'" + tokens[0].getType() + "\'.")
            print ("Stopping program")
            sys.exit()
        
        self.match(tokens, Token(TokenType.REGISTER, ""))
        self.parseAux(tokens)

        
    



            

