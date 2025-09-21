import re


class FiniteAutomata:
    def __init__(self, _filename):
        self.states = []
        self.alphabet = []
        self.transitions = {}
        self.initial_state = ""
        self.final_states = []
        self.filename = _filename
        self.read_from_file()

    def read_from_file(self):
        with open(self.filename, 'r') as program:
            line_nr = 0
            is_transition = False
            for line in program:
                if line_nr == 1:
                    for state in re.split('[ ,Q=\n]', line):
                        if state != '':
                            self.states.append(state)
                if line_nr == 2:
                    for letter in re.split('[, E=\n]', line):
                        if letter != '':
                            self.alphabet.append(letter)
                if line == "start\n":
                    is_transition = True
                    continue
                if line == "end\n":
                    is_transition = False
                    continue
                if is_transition:
                    is_last = False
                    is_first = True
                    first = ""
                    last = ""
                    letters = []
                    for word in re.split('[, \[\]\n]', line):
                        if word == '':
                            continue
                        if is_first:
                            first = word
                            is_first = False
                        if is_last:
                            last = word

                        if word == "->":
                            is_last = True
                        if word != '' and word != first and word != last and word != '->':
                            letters.append(word)
                    for letter in letters:
                        self.transitions[(first, letter)] = last
                    continue
                if re.split("[= ]", line)[0] == "q0":
                    self.initial_state = re.split("[= ]", line)[3]
                    continue
                if re.split("[= ,]", line)[0] == "F":
                    for word in re.split("[= ,]", line):
                        if word == "F":
                            continue
                        if word != '':
                            self.final_states.append(word)
                    continue
                line_nr += 1

    def print_fa(self):
        print("M = {Q, E, RO, q0, F}\n")
        print(f"Q = {self.states}\n")
        print(f"E = {self.alphabet}\n")
        print(f"RO = {self.transitions}\n")
        print(f"q0 = {self.initial_state}\n")
        print(f"F = {self.final_states}\n")

    def check_word_if_integer_constant(self, word):
        state = 'q0'
        for letter in word:
            state = self.transitions.get((state, letter))
            if state is None:
                return

        if state not in ['q5', 'q6']:
            return False
        return True

    def check_word_if_identifier(self, word):
        state = 'q0'
        for letter in word:
            state = self.transitions.get((state, letter))
            if state is None:
                return

        if state not in ['q2']:
            return False
        return True