class ParserOutput:
    def __init__(self, parsing_table):
        """
        Initialize the ParserOutput with the given parsing table.
        :param parsing_table: The parsing table to be transformed into a representation.
        """
        self.parsing_table = parsing_table
        self.representation = self.transform_parsing_table_into_representation()

    def transform_parsing_table_into_representation(self):
        """
        Transform the parsing table into a representation suitable for printing and saving.
        :return: A list of tuples representing the parsing table.
        """
        representation = []
        for non_terminal, rules in self.parsing_table.items():
            for terminal, rule in rules.items():
                if rule is not None:
                    father = non_terminal
                    sibling = terminal
                    representation.append((father, sibling, rule))
        return representation

    def print_to_screen(self):
        """
        Print the representation of the parsing table to the screen.
        """
        for father, sibling, rule in self.representation:
            print(f'Father: {father}, Sibling: {sibling}, Rule: {rule}')

    def print_to_file(self, filename):
        """
        Print the representation of the parsing table to a file.
        :param filename: The name of the file to save the representation.
        """
        with open(filename, 'w') as file:
            for father, sibling, rule in self.representation:
                file.write(f'Father: {father}, Sibling: {sibling}, Rule: {rule}\n')

    def parse(self, input_sequence):
        """
        Parse the input sequence using the parsing table.
        :param input_sequence: The sequence of input symbols to be parsed.
        :return: True if the sequence is accepted, False otherwise.
        """
        input_sequence += '$'
        stack = ['$']
        stack.append(next(iter(self.parsing_table)))  # Start symbol of the grammar
        input_index = 0

        while len(stack) > 0:
            top = stack.pop()

            if top in self.parsing_table:
                rule = self.parsing_table[top].get(input_sequence[input_index])
                if rule is None:
                    return False

                for symbol in reversed(rule):
                    if symbol != 'epsilon':
                        stack.append(symbol)

            elif top in [*self.parsing_table.keys(), '$']:
                if top != input_sequence[input_index]:
                    return False

                input_index += 1

            elif top == 'epsilon':
                continue

            else:
                raise ValueError(f"Invalid symbol in stack: {top}")

        return input_index == len(input_sequence)
