#fix indenting of match
#https://emacs.stackexchange.com/questions/69291/how-can-i-make-python-mode-correctly-indent-pythons-match-statement
class krivine_machine:
    term = []
    stack = []
    environment = []
    #apply a to b
    def apply (self):

        self.stack = [self.term[ -1 ] , self.environment ]

        if type(self.term[-2]) == int:
            self.term=[self.term[-2]]
        else:
            self.term = self.term[ -2 ]
            
        #self.environment unchanged

        #perform lambda abstraction
    def abstract (self):
          
        self.environment = self.stack
         
        self.stack = []
            
        self.term = self.term[1:]

         #zero instruction
    def zero (self):


        if type(self.environment[0]) == int:
            self.term = [self.environment[ 0 ]]
        else: 
            self.term = self.environment[ 0 ]
            
        self.environment =  self.environment[ 1 ]

        #self.stack unchanged

        #success instruction

    def success (self):


        self.term[0] = self.term[0] - 1

        self.environment = self.environment[ 1 ]

        #stack unchanged

        #select which function to run
    def choose(self):
        print(self.term)
        print(self.stack)
        print(self.environment)
        if self.term[0] == -1:
   #         print("abstract")
            self.abstract(self)
        elif len(self.term) == 1:
            if self.term[-1] == 0 :
  #              print("zero")
                self.zero(self)
            else :
 #               print("success")
                self.success(self)
        else :
#            print("apply")
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

        
     

        

            
                            
