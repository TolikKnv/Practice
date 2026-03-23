import time
from typing import Dict, Tuple



INITIAL_TAPE = "10101000000000010000111110"
INITIAL_STATE = "q0"
HALT_STATE = "qf"
BLANK_SYMBOL = "#"


TRANSITION_RULES = {
    'q0 0': 'q0 1 R',
    'q0 1': 'q0 0 R',
    'q0 #': 'qf # N'
}


class TuringMachine:

    def __init__(self, tape_str: str, initial_state: str, halt_state: str, blank: str, rules: Dict[str, str]):
        self.tape = {i: char for i, char in enumerate(tape_str)}
        self.state = initial_state
        self.halt_state = halt_state
        self.blank = blank
        self.rules = rules
        self.head_position = 0
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

        print(f"Step: {self.step_count} | Current State: {self.state}")
        print(tape_line)
        print(head_pointer)
        print("-" * 40)

    def step(self) -> bool:
        current_char = self.tape.get(self.head_position, self.blank)
        lookup_key = f"{self.state} {current_char}"

        if lookup_key not in self.rules:
            print(f"CRITICAL ERROR: No transition rule found for state '{self.state}' and character '{current_char}'")
            return False


        action = self.rules[lookup_key].split()
        if len(action) != 3:
            print(f"CRITICAL ERROR: Invalid rule format for '{lookup_key}'")
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
            print(f"CRITICAL ERROR: Invalid movement command '{movement}'")
            return False

        self.step_count += 1
        return True

    def run(self, delay: float = 0.4):
        print(">>> INITIALIZING TURING MACHINE <<<")
        self.display()

        while self.state != self.halt_state:
            if not self.step():
                break

            time.sleep(delay)
            self.display()

        if self.state == self.halt_state:
            print(">>> EXECUTION COMPLETED SUCCESSFULLY <<<")


def main():
    tm = TuringMachine(
        tape_str=INITIAL_TAPE,
        initial_state=INITIAL_STATE,
        halt_state=HALT_STATE,
        blank=BLANK_SYMBOL,
        rules=TRANSITION_RULES
    )
    tm.run()


if __name__ == "__main__":
    main()