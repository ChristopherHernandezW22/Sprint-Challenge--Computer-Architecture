"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
ADD = 0b10100000
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110

SP = 7

# greater gtf == > flag, ltf == < flag, etf == = flag
ltf = 0b100
gtf = 0b010
etf = 0b001


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.running = True
        self.flags = 0b00000001
        self.branch_table = {
            HLT: self.HLT_op,
            LDI: self.LDI_op,
            PRN: self.PRN_op,
            ADD: self.ADD_op,
            MUL: self.MUL_op,
            PUSH: self.PUSH_op,
            POP: self.POP_op,
            CALL: self.CALL_op,
            RET: self.RET_op,
            CMP: self.CMP_op,
            JMP: self.JMP_op,
            JEQ: self.JEQ_op,
            JNE: self.JNE_op
        }

        