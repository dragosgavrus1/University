import re
from symboltables import ConstantSymbolTable, IdentifierSymbolTable
from fa import FiniteAutomata

IDENTIFIER = 0
CONSTANT = 1
OPERATOR = 2
RESERVED_WORD = 3
SEPARATOR = 4

class Scanner():
    def __init__(self, filename, token_file):
        self.filename = filename
        self.token_file = token_file
        self.constant_table = ConstantSymbolTable()
        self.identifiers_table = IdentifierSymbolTable()
        self.pif = []
        self.reserved_words = {}
        self.operators = {}
        self.separators = {}
        self.get_tokens()
        self.constants_count = 0
        self.finite_automata = FiniteAutomata('FA.in')


    def scan_file(self):
        with open(self.filename, 'r') as program:
            line_count = 0
            for line in program:
                line_count += 1
                line = line.rstrip('\n')
                operators_and_separators = r'(;|==|=|!=|\+=|-=|\*=|\/=|<=|>=|[\+\-\*=\/<>!;\[\]\{\}\(\),;]|\|\||&&)'

                for word in re.split(operators_and_separators, line):
                    is_string = False
                    if (word.startswith('"') or word.startswith(' "')) and word.endswith('"'):
                        is_string = True
                        word = word.replace(' ', '').replace('"', '')
                        if self.constant_table.get_position(word) is None:
                            self.constant_table.add_constant(word, self.constants_count)
                            self.pif.append((CONSTANT, self.constant_table.get_position(word)))
                            self.constants_count += 1
                    elif (word.startswith("'") or word.startswith(" '")) and word.endswith("'"):
                        is_string = True
                        word = word.replace(' ', '').replace("'", '')
                        if self.constant_table.get_position(word) is None:
                            self.constant_table.add_constant(word, self.constants_count)
                            self.pif.append((CONSTANT, self.constant_table.get_position(word)))
                            self.constants_count += 1
                    if not is_string:
                        for word in word.split():
                            if word == '':
                                continue
                            if word in self.reserved_words.keys():
                                self.pif.append((self.reserved_words.get(word), 0))
                            elif word in self.operators.keys():
                                self.pif.append((self.operators.get(word), 0))
                            elif word in self.separators.keys():
                                self.pif.append((self.separators.get(word), 0))
                            elif self.is_constant(word):
                                if self.constant_table.get_position(word) is None:
                                    self.constant_table.add_constant(word, self.constants_count)
                                    self.pif.append((CONSTANT, self.constant_table.get_position(word)))
                                    self.constants_count += 1
                            elif self.is_identifier(word):
                                if self.identifiers_table.get_position(word) is None:
                                    self.identifiers_table.add_identifier(word, None)
                                self.pif.append((IDENTIFIER, self.identifiers_table.get_position(word)))
                            else:
                                print(f'Lexical error at line {line_count}\n')
                                return
            print('Lexically correct')

        with open('ST.out', 'w') as output:
            print(str(self.identifiers_table.table))
            output.write(str(self.identifiers_table.table))
            print(str(self.constant_table.table))
            output.write(str(self.constant_table.table))
        with open('PIF.out', 'w') as output:
            for key, value in self.pif:
                output.write(f"{key} - {value}\n")
        self.finite_automata.print_fa()


    def get_tokens(self):
        should_add_in = RESERVED_WORD
        line_no = 2
        with open(self.token_file, 'r') as token_file:
            for line in token_file:
                line = line.replace('\n', '')
                if line == '[reserved_words]':
                    continue
                if line == '[operators]':
                    should_add_in = OPERATOR
                    continue
                if line == '[separators]':
                    should_add_in = SEPARATOR
                    continue
                if should_add_in == RESERVED_WORD:
                    self.reserved_words[line] = line_no
                if should_add_in == OPERATOR:
                    self.operators[line] = line_no
                if should_add_in == SEPARATOR:
                    self.separators[line] = line_no
                line_no += 1

    def is_identifier(self, string):
        return self.finite_automata.check_word_if_identifier(string)

    def is_constant(self, string):
        pattern_char = re.compile("'[a-zA-Z0-9]'")
        pattern_string = re.compile('"[a-zA-Z0-9]*"')
        if self.finite_automata.check_word_if_integer_constant(string) or pattern_char.fullmatch(string) or pattern_string.fullmatch(string):
            return True
        return False
