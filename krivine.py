#fix indenting of match
#https://emacs.stackexchange.com/questions/69291/how-can-i-make-python-mode-correctly-indent-pythons-match-statement
class krivine_machine:
    term = []
    stack = []
    environment = []
    #apply a to b
    def apply (self):
          
        self.stack = [ [self.term[ -1 ] , self.environment ] ,
            self.stack
            ]
            
        self.term = self.term[ -2 ]
            
        #self.environment unchanged

        #perform lambda abstraction
    def abstract (self):
          
        self.environment = [ self.stack[ 0 ] , self.environment ]
         
        self.stack = self.stack[ 1 ]
            
        self.term = self.term[ -1 ]

         #zero instruction
    def zero (self):

        self.term = self.environment[ 0 ][ 0 ]
            
        self.environment =  self.environment[ 0 ][ 1 ]

        #self.stack unchanged

        #success instruction

    def success (self):

        self.term[ -1 ] = self.term[ -1 ] - 1

        self.environment = self.environment[ 1 ]

    def choose(self):
        if type(self.term[-1]) == int:
            if self.term[-1] == 0 :
                self.zero(self)
            else : 
                self.success(self)
        elif self.term[-2] == -1:
            self.abstract(self)
        else :
            self.apply(self)
        print(self.term)
            
    def run(self, input_lambda):
        self.stack = []
        self.environment = []
        self.term = input_lambda
        
        self.choose(self);
        while (len(self.stack) and len(self.environment)):
            self.choose(self);
        return self.stack

krivine_machine.run(krivine_machine, [[-1,0,0],[-1,0]])

        
     

        

            
                            
