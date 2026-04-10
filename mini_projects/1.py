import time


INITIAL_TAPE = "10101"
INITIAL_STATE = "q0"
HALT_STATE = "qf"
BLANK_SYMBOL = "#"


TRANSITION_RULES = {
    'q0 #': 'qf # N',
    'q0 0': 'q1 # R',
    'q0 1': 'q2 # R',

    'q1 0': 'q1 0 R',
    'q1 1': 'q1 1 R',
    'q1 #': 'q3 # L',

    'q2 0': 'q2 0 R',
    'q2 1': 'q2 1 R',
    'q2 #': 'q4 # L',

    'q3 0': 'q5 # L',
    'q3 1': 'qf 1 N',
    'q3 #': 'qf # N',

    'q4 0': 'qf 1 N',
    'q4 1': 'q6 # L',
    'q4 #': 'qf # N',

    'q5 0': 'q5 0 L',
    'q5 1': 'q5 1 L',
    'q5 #': 'q0 # R',

    'q6 0': 'q6 0 L',
    'q6 1': 'q6 1 L',
    'q6 #': 'q0 # R',
}


class TuringMachine:

    def __init__(self, tape_str, initial_state, halt_state, blank, rules):
        self.tape = {i: char for i, char in enumerate(tape_str)}
        self.head_position = 0
        self.state = initial_state
        self.halt_state = halt_state
        self.blank = blank
        self.rules = rules
        self.step_count = 0

    def display(self):
        keys = self.tape.keys()
        if not keys:
            min_index, max_index = self.head_position - 1, self.head_position + 1
        else:
            min_index = min(min(keys), self.head_position) - 1
            max_index = max(max(keys), self.head_position) + 1

        tape_line = ""
        head_pointer = ""

        for i in range(min_index, max_index + 1):
            char = self.tape.get(i, self.blank)
            if i == self.head_position:
                tape_line += f"[{char}]"
                head_pointer += " ^ "
            else:
                tape_line += f" {char} "
                head_pointer += "   "

        print(f"Step: {self.step_count} | State: {self.state}")
        print(tape_line)
        print(head_pointer)
        print("-" * 50)

    def step(self) -> bool:
        current_char = self.tape.get(self.head_position, self.blank)
        lookup_key = f"{self.state} {current_char}"

        if lookup_key not in self.rules:
            print(f"ERROR: No rule for ({self.state}, {current_char})")
            return False

        action = self.rules[lookup_key].split()
        if len(action) != 3:
            print(f"ERROR: Invalid rule format: {lookup_key}")
            return False

        next_state, next_char, movement = action

        self.tape[self.head_position] = next_char

        self.state = next_state

        if movement == 'R':
            self.head_position += 1
        elif movement == 'L':
            self.head_position -= 1
        elif movement == 'N':
            pass
        else:
            print(f"ERROR: Invalid movement {movement}")
            return False

        self.step_count += 1
        return True

    def run(self, delay=0.01):
        self.display()

        while self.state != self.halt_state:
            if not self.step():
                break
            self.display()
            time.sleep(delay)



def main():
    tm = TuringMachine(
        INITIAL_TAPE,
        INITIAL_STATE,
        HALT_STATE,
        BLANK_SYMBOL,
        TRANSITION_RULES
    )
    tm.run()


if __name__ == "__main__":
    main()