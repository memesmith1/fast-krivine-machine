#fix indenting of match
#https://emacs.stackexchange.com/questions/69291/how-can-i-make-python-mode-correctly-indent-pythons-match-statement
class krivine_machine:
      term = []
      stack = []
      environment = []
      #apply a to b
      def apply ():
            
            self.stack = [ [term[ -1 ] , self.environment ] ,
                           self.stack
                          ]
            
            self.term = term[ -2 ]
            
            #self.environment unchanged

      #perform lambda abstraction
      def abstract ():
            
            self.environment = [ self.stack[ 0 ] , self.environment ]
            
            self.stack = self.stack[ 1 ]
            
            self.term = self.term[ -1 ]

      #zero instruction
      def zero ():

            self.term = self.environment[ 0 ][ 0 ]
            
            self.environment =  self.environment[ 0 ][ 1 ]

            #self.stack unchanged

      #succ instruction
      def success ():

            self.term = self.term - 1

            self.environment = self.environment[ 1 ]

            #self.stack unchanged

      def choose () :
            match self.term[-1].isnumeric() :
                case True :
                    match self.term[-1] :
                        case 0 :
                        self.zero()
                        
                        case _ :
                        self.success()
            
                  case False :
                      match self.term[ -2 ]
                          case -1 :
                              self.app()
                        case _ :
                            self.abstract()
      def load () :

            
                            
