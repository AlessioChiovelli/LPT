import lark
class scanner(lark.Transformer):
      NUMBER = int
      def __init__(self):
          self.vars = {}
        
      def operations(self,args):##Printing the value of z
        self.vars['z'] = args[-1]
        return f'z = {args[-1]}\nvars: {self.vars}'
          
      def assignment_with_number(self,args):
          self.vars[args[0]] = args[1]  ##Assign the variable "name" and value to the dictionary
          return args[1]  ##returning the value of the var
        
      def assignment_without_number(self,args):
          self.vars[args[0]] = 0  ##Assign the variable "name" and value to the dictionary
          return 0  ##returning the value of the var
        
      def var(self,args):#Storing the variables
          try:
            return self.vars[args[0]]
          except KeyError:
            raise Exception("Variable %s not defined" % args[0])
          
      def if_block(self,args):
            #args[0]: Result of the control statement
            #args[1]: Block of code if the control statement is true 
          try:
            if args[0]:return args[1]
            return None#the control statement is false
          except KeyError:
            raise None
      
      def simple_condition(self,args):
            #args[0]: Returning the result of the if
            #args[1]: Returning the result of the else
          try:
            if args[0]!=None:return args[0]
            return args[1]
          except KeyError:
            raise None
      
      def composed_condition(self,args):
            #args[0]: Returning the result of the if
            #args[1]: Returning the result of the nested conditions
          try:
            if args[0]!=None:return args[0]
            return args[1]
          except KeyError:
            raise None
      
      def assignment_z_with_number(self,args):
          self.vars[args[0]] = args[1]  ##Assign the variable z and value to the dictionary
          return args[1]
      
      def assignment_z_without_number(self,args):
          self.vars[args[0]] = 0  ##Assign the variable z and value to the dictionary
          return 0
        
      #controls divided by variable-number / variable-variable confrontation
      def minor_of_const(self,args):
          return self.vars[args[0]] < args[1]
            
      def different_of_const(self,args):
          return self.vars[args[0]] != args[1]
            
      def major_of_const(self,args):
          return self.vars[args[0]] > args[1]

      def equal_of_const(self,args):
          return self.vars[args[0]] == args[1]

      def minor_of_variable(self,args):
          return self.vars[args[0]] < self.vars[args[1]]

      def different_of_variable(self,args):
          return self.vars[args[0]] != self.vars[args[1]]

      def major_of_variable(self,args):
          return self.vars[args[0]] > self.vars[args[1]]

      def equal_of_variable(self,args):
          return self.vars[args[0]] == self.vars[args[1]]
        
def transformer(string_to_parse:str = 'x=5;y;x=7;if(x>7){z=3;}else if(x==8){z=5;}else{z=11;}'):
  project_transformer = lark.Lark.open("grammar.lark",rel_to=__file__,start="operations",parser='lalr',transformer=scanner())
  try:
    result = project_transformer.parse(string_to_parse)
    return result
  except lark.UnexpectedToken as error: return error.get_context(string_to_parse)
  except lark.UnexpectedInput as error: return error.get_context(string_to_parse)
  except Exception as error: return error
  
  # try:
    #   print(project_transformer.parse(string_to_parse))
    # #Error(S)
    # except lark.UnexpectedToken as error:
    #   print(error.get_context(string_to_parse),end='')
    #   print("Unexpected token %s " % error.token)
    # except lark.UnexpectedInput as error:
    #     print("Parser error")
    #     print(error.get_context(string_to_parse))
    # except Exception as error:
    #     print(error)