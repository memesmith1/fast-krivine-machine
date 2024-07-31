#fix indenting of match
#https://emacs.stackexchange.com/questions/69291/how-can-i-make-python-mode-correctly-indent-pythons-match-statement
class krivine_machine:
    term = []
    stack = []
    environment = []
    #apply a to b
    def apply (self):

        print("apply\n")  
        self.stack = [self.term[ -1 ] , self.environment ]

        if type(self.term[-2]) == int:
            self.term=[self.term[-2]]
        else:
            self.term = self.term[ -2 ]
            
        #self.environment unchanged

        #perform lambda abstraction
    def abstract (self):
        print("abstract\n")
          
        self.environment = self.stack
         
        self.stack = []
            
        self.term = self.term[1:]

         #zero instruction
    def zero (self):

        print("zero\n")
#        print("environment:\n")
 #       print(self.

        if type(self.environment[0]) == int:
            self.term = [self.environment[ 0 ]]
        else: 
            self.term = self.environment[ 0 ]
            
        self.environment =  self.environment[ 1 ]

        #self.stack unchanged

        #success instruction

    def success (self):

        print("success\n")

        self.term[ -1 ] = self.term[ -1 ] - 1

        self.environment = self.environment[ 1 ]

    def choose(self):
        print(self.term)
        print(self.stack)
        print(self.environment)
        if self.term[0] == -1:
            self.abstract(self)
        elif len(self.term) == 1:
            if self.term[-1] == 0 :
                self.zero(self)
            else : 
                self.success(self)
        else :
            self.apply(self)

            
    def run(self, input_lambda):
        self.stack = []
        self.environment = []
        self.term = input_lambda
        
        self.choose(self);
        while (len(self.stack) or len(self.environment)):
            self.choose(self);
            
        return self.term

print(krivine_machine.run(krivine_machine, [[-1,0,0],[-1,0]]))

        
     

        

            
                            
