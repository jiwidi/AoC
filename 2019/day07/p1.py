from itertools import permutations


def code_one(code, pointer, p1mode, p2mode, input, output):
    p1 = (
        code[pointer + 1] if p1mode else code[code[pointer + 1]]
    )  # Handle position or inmediate modes
    p2 = code[pointer + 2] if p2mode else code[code[pointer + 2]]
    code[code[pointer + 3]] = p1 + p2
    return pointer + 4  # Return how many instructions jump


def code_two(code, pointer, p1mode, p2mode, input, output):
    p1 = code[pointer + 1] if p1mode else code[code[pointer + 1]]
    p2 = code[pointer + 2] if p2mode else code[code[pointer + 2]]
    code[code[pointer + 3]] = p1 * p2
    return pointer + 4


def code_three(code, pointer, p1mode, p2mode, input, output):
    code[code[pointer + 1]] = input[0]
    input[:] = input[1:]
    return pointer + 2


def code_four(code, pointer, p1mode, p2mode, input, output):
    p1 = code[pointer + 1] if p1mode else code[code[pointer + 1]]
    output[:] = [p1]
    # print(f"output {p1}") #(?)
    return pointer + 2


def code_five(code, pointer, p1mode, p2mode, input, output):
    p1 = code[pointer + 1] if p1mode else code[code[pointer + 1]]
    p2 = code[pointer + 2] if p2mode else code[code[pointer + 2]]
    if p1 != 0:
        return p2
    return pointer + 3


def code_six(code, pointer, p1mode, p2mode, input, output):
    p1 = code[pointer + 1] if p1mode else code[code[pointer + 1]]
    p2 = code[pointer + 2] if p2mode else code[code[pointer + 2]]
    if p1 == 0:
        return p2
    return pointer + 3


def code_seven(code, pointer, p1mode, p2mode, input, output):
    p1 = code[pointer + 1] if p1mode else code[code[pointer + 1]]
    p2 = code[pointer + 2] if p2mode else code[code[pointer + 2]]
    if p1 < p2:
        code[code[pointer + 3]] = 1
    else:
        code[code[pointer + 3]] = 0
    return pointer + 4


def code_eight(code, pointer, p1mode, p2mode, input, output):
    p1 = code[pointer + 1] if p1mode else code[code[pointer + 1]]
    p2 = code[pointer + 2] if p2mode else code[code[pointer + 2]]
    if p1 == p2:
        code[code[pointer + 3]] = 1
    else:
        code[code[pointer + 3]] = 0
    return pointer + 4


def decode_op(i):
    i = [int(n) for n in str(i)]
    listI = [
        0 for u in range(4 - len(i))
    ] + i  # Make it to consistent length to decode the operation code
    p1mode = listI[1]
    p2mode = listI[0]
    opcode = int(str(listI[2]) + str(listI[3]))
    return p1mode, p2mode, opcode


ops = {  # This functions are assign by reference, so they will modify the code without returning the new version
    1: code_one,
    2: code_two,
    3: code_three,
    4: code_four,
    5: code_five,
    6: code_six,
    7: code_seven,
    8: code_eight,
}


class Amp:
    def __init__(self, code):
        self.code = code[:]
        self.prog = code[:]
        self.output = [0]
        self.input_counter = 0
        self.halt = False
        self.pointer = 0


def run_amp(phase, input, amp):
    input = [phase] + input
    while amp.pointer < len(amp.code):
        p1mode, p2mode, opcode = decode_op(amp.code[amp.pointer])
        # print("Doing op {}, {}".format(opcode, code[i:i+4]))
        if opcode in ops.keys():
            amp.pointer = ops[opcode](
                amp.code, amp.pointer, p1mode, p2mode, input, amp.output
            )
            if opcode == 4:
                return amp
        else:
            if opcode == 99:
                # print('yo')
                amp.halt = True
                break
            i += 1
    return amp


def sim_thrusters_p1(content, range_amplifiers):
    r = []
    for sequence in permutations(range_amplifiers, 5):
        amps = [Amp(content.copy()) for i in range(5)]
        # A
        amps[0] = run_amp(sequence[0], [0], amps[0])
        # B
        amps[1] = run_amp(sequence[1], amps[0].output, amps[1])
        # C
        amps[2] = run_amp(sequence[2], amps[1].output, amps[2])
        # D
        amps[3] = run_amp(sequence[3], amps[2].output, amps[3])
        # E
        amps[4] = run_amp(sequence[4], amps[3].output, amps[4])
        r.append(amps[4].output[-1])
    return r


def read_input(path):
    return [int(x) for x in open(path).read().split(",")]


if __name__ == "__main__":
    # ask for user input
    # Read the input.txt
    content = read_input("input.txt")
    # Solve p1
    r = sim_thrusters_p1(content, range_amplifiers=[0, 1, 2, 3, 4])
    print(f"--- Part One --- \n{max(r)}")
