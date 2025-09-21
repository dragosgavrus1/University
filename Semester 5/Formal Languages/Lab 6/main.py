from parser_output import ParserOutput
from parser import Parser
from grammar import Grammar

# Load grammar from file
grammar = Grammar.fromFile("g1.txt")

# Create a parser and compute the parsing table
parser = Parser(grammar=grammar)
parser.computeCanonicalCollection()
parser.computeTableActions()
parsing_table = parser.table.actionsForStates

# Create a ParserOutput object
parser_output = ParserOutput(parsing_table)

# Print representation to screen
print("Parsing Table Representation:")
parser_output.print_to_screen()

# Save representation to a file
output_file = "parsing_table_representation.txt"
parser_output.print_to_file(output_file)
print(f"Parsing table representation saved to {output_file}")

# Parse an example input sequence
input_sequence = "ac"
print(f"Parsing sequence: {input_sequence}")
if parser_output.parse(input_sequence):
    print("Sequence is accepted.")
else:
    print("Sequence is not accepted.")


