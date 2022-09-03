import lark
import pydot
from utils.parser import parser
from utils.transformer import transformer

if __name__ == '__main__':
    #Trial expression to parse for testing the parser
    e = 'x=5;y;x=7;if(x>7){z=3;}else if(x==8){z=5;}else{z=11;}'
    parser_result = parser(string_to_parse = e)
    #Transformer adopted
    transformer_result = transformer(string_to_parse = e)
    grammar = lark.Lark.open("utils/grammar.lark",rel_to=__file__,start="operations",ambiguity="explicit")

    
    print(f'''
          GRAMMAR:
          {grammar}
          Parsed Tree of Trial:
          {parser_result.pretty()}
          Transformer Result:
          {transformer_result}
          ''')

    #Command line tool to test [Parser][Transformer]
    while True:
          #GUIDELINE
          print(f'''\n\nCommands Available: \n['break'] : End program \n['start parsing'] : Start the parsing of a string (which is given in input) and print the tree \n['transformer']\n\n''')
          command = input('Command> ')
          if command == 'break':break         #Stopping the tool
          if command == 'start parsing':      #Parser
                string_to_parse = ''
                print(f'\n\nStart of the parsing. When you\'re finished you\'ll be asked to print parse Tree.\nWhen you\'re asked, type \'y\' to print it\n\n')
                while True:
                      string_to_add = input(f'>{string_to_parse}')
                      string_to_parse += string_to_add
                      stop_and_print = input('stop and print? [\'y\' / \'n\'] ->') #Printing the Tree and getting back on the commands
                      if stop_and_print == 'y':break
                result_of_parser = parser(string_to_parse)
                print(result_of_parser.pretty())
          if command == 'transformer':    #Transformer
            while True:
                line = input('(TRANSFORMER)Input a line to parse>  ')
                if input('stop? [\'y\' / \'n\'] ->')=='y':break
            result_of_transformer = transformer(line)
            print(result_of_transformer)