import lark
import pydot

def parser(string_to_parse : str = 'x=5;y;x=7;if(x>7){z=3;}else if(x==8){z=5;}else{z=11;}'):
    project_parser = lark.Lark.open("grammar.lark",rel_to=__file__,start="operations",ambiguity="explicit")
    #Printing (on the terminal) and saving the .pdf/.svg Trees
    try:
        parseTree = project_parser.parse(string_to_parse)
        graph = lark.tree.pydot__tree_to_graph(parseTree, "TB")
        graph.write_svg(f"svg/Tree_{string_to_parse}.svg")
        graph.write_pdf(f"pdf/Tree_{string_to_parse}.pdf")
        # print("Saving PDF version of tree\n\n\n\n")
        # print("Tree Saved!\n\n\n\n")
        # print(f"*** Parse tree pretty print\n{parseTree.pretty()}")
        
        return parseTree
    #Error
    except Exception as error:
        print(error)
    # else:
    #     try:
    #         result = project_parser.parse(string_to_parse)
    #         return result
    #     except Exception as error:return error