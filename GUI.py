from utils.parser import parser
from utils.transformer import transformer
import PySimpleGUI as sg

def Parser(string_to_analize):
    result = parser(string_to_analize)
    Button_font = ("Arial",13)
    Button_layout = [
        [sg.Text(result.pretty(),font = Button_font, auto_size_text = True),]
        ]
    PopupWindow = sg.Window(f'Parser Result',Button_layout,font = Button_font,resizable=True)
    while True:
        event, _ = PopupWindow.read()
        if event == sg.WINDOW_CLOSED:
            break
    PopupWindow.close()
    
def Transformer(string_to_analize):
    result = transformer(string_to_analize)
    Button_font = ("Arial",13)
    Button_layout = [
        [sg.Text(result,font = Button_font, auto_size_text = True)]
        ]
    PopupWindow = sg.Window(f'Transformer Result',Button_layout,font = ("Arial"),resizable=True)
    while True:
        event, _ = PopupWindow.read()
        if event == sg.WINDOW_CLOSED:
            break
    PopupWindow.close()
    
def Info(info_message,title):
    sg.theme('Reddit')
    Button_font = ("Arial",13)
    layout = [
        [sg.Text(info_message,font = Button_font)]
        ]
    PopupWindow = sg.Window(f'Info of the {title}',layout,font = ("Arial"),resizable=True)
    while True:
        event, _ = PopupWindow.read()
        if event == sg.WINDOW_CLOSED:
            break
    PopupWindow.close()

if __name__ == "__main__":
    sg.theme('Reddit')
    initial_text_display = '''Welcome to Alessio Chiovelli and Andrea Porri's first project work for LPT!\nThe following program can:\n-----> Scan throught strings of code(Transformer option)\n-----> Parse an input string (Parser)\n\nFeel free to try!'''
    Button_font = ("Arial",16)


    # # All the stuff inside your window.
    layout = [  
            [sg.Text(initial_text_display,font = Button_font)],
            [sg.VerticalSeparator()],
            [sg.VerticalSeparator()],
            [sg.VerticalSeparator()],
            [sg.VerticalSeparator()],
            [sg.VerticalSeparator()],
            [sg.VerticalSeparator()],
            [
                sg.Text('Input String -->',font = Button_font),
                sg.Input('x=5;y;x=7;if(x>7){z=3;}else if(x==8){z=5;}else{z=11;}',font = Button_font, key = '--InputString--')
                ],
            [sg.VerticalSeparator()],
            [
                sg.Button(button_text = "Parser",key = '--Parser--',font = Button_font),
                sg.Button(button_text = "Transformer",key = '--Transformer--',font = Button_font),
                sg.Button(button_text = "Parser-Info",key = '--Parser-Info--',font = Button_font),
                sg.Button(button_text = "Transformer-Info",key = '--Transformer-Info--',font = Button_font),
                sg.Button(button_text = "Grammar-Info",key = '--Grammar-Info--',font = Button_font),
                sg.Button(button_text = "QUIT",key = '--QUIT--',font = Button_font)
            ]
            ]

    grammar = '''
        ?operations: (assignment_var)+ (composed_condition)* (simple_condition)*
            
        condition: composed_condition | simple_condition

        composed_condition: if_block "else" simple_condition

        simple_condition: if_block (else_block)?

        if_block: "if" conditional_blocks operator_block -> if_block

        else_block: "else" operator_block -> else_block

        ?assignment_var: assignment_with_number|assignment_without_number

        assignment_with_number : VARIABLES "=" NUMBER ";" -> assignment_with_number

        assignment_without_number : VARIABLES ";"  -> assignment_without_number

        ?operator_block: "{" VARIABLE_Z "=" NUMBER ";}" -> assignment_z_with_number
                        |  "{" VARIABLE_Z ";}" -> assignment_z_without_number

        VARIABLES: "x"|"y"

        VARIABLE_Z: "z"

        conditional_blocks: "(" VARIABLES "<" NUMBER ")" -> minor_of_const
                            |"(" VARIABLES "<" VARIABLES ")" -> minor_of_variable
                            |"(" VARIABLES "!=" NUMBER ")" -> different_of_const
                            |"(" VARIABLES "!=" VARIABLES ")" -> different_of_variminor_of_variable
                            |"(" VARIABLES ">" NUMBER ")" -> major_of_const
                            |"(" VARIABLES ">" VARIABLES ")" -> major_of_variminor_of_variable
                            |"(" VARIABLES "==" NUMBER ")" ->  equal_of_const
                            |"(" VARIABLES "==" VARIABLES ")" -> equal_of_variminor_of_variable
                    
        %import common.ESCAPED_STRING
        %import common.NUMBER
        %import common.WS_INLINE
        %ignore WS_INLINE
        '''
    Transformer_info ="Info"
    Parser_info ="Info"
    # Create the Window
    window = sg.Window('Transformers and Parser',layout,resizable=True,background_color = "gray",element_padding = 2,scaling = 3)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '--QUIT--': # if user closes window or clicks cancel
            break
        if event == '--Parser--':
            Parser(values['--InputString--'])
        if event == '--Transformer--':
            Transformer(values['--InputString--'])
        if event == '--Transformer-Info--':
            Info(Transformer_info,"Transformer")
        if event == '--Parser-Info--':
            Info(Parser_info,"Parser")
        if event == '--Grammar-Info--':
            Info(grammar,"Grammar")
            

    window.close()


