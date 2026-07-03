# Day 10 — 2026-07-03 to 2026-07-04

Completed FSM problems: **4**. Every entry has a full-page HDLBits capture containing the question, complete submitted answer, and visible `Status: Success!` result. The original handwritten, partial-attempt, and ChatGPT discussion images remain beside the matching problem for revision.

## Index

| # | Problem | Problem note | Full question + answer | Solution | Source |
|---:|---|---|---|---|---|
| 155 | Q3a: FSM | [Counter/FSM discussion](problems/Day%2010/155-exams__2014_q3fsm.md) | [Screenshot](images/Day%2010/155-exams__2014_q3fsm-question-and-answer.png) | [Code](solutions/Day%2010/155-exams__2014_q3fsm.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2014_q3fsm) |
| 156 | Q3b: FSM | [Complete state-machine note](problems/Day%2010/156-exams__2014_q3bfsm.md) | [Screenshot](images/Day%2010/156-exams__2014_q3bfsm-question-and-answer.png) | [Code](solutions/Day%2010/156-exams__2014_q3bfsm.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2014_q3bfsm) |
| 157 | Q3c: FSM logic | [Handwritten derivation and correction](problems/Day%2010/157-exams__2014_q3c.md) | [Screenshot](images/Day%2010/157-exams__2014_q3c-question-and-answer.png) | [Code](solutions/Day%2010/157-exams__2014_q3c.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2014_q3c) |
| 158 | Q6c: FSM one-hot next-state logic | [Incoming-arrow derivation](problems/Day%2010/158-exams__m2014_q6c.md) | [Screenshot](images/Day%2010/158-exams__m2014_q6c-question-and-answer.png) | [Code](solutions/Day%2010/158-exams__m2014_q6c.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q6c) |

## Revision priorities

- Distinguish phase state from counters and other datapath registers.
- Separate the state register, next-state logic, and Moore output decode.
- Derive a requested next-state bit from the selected bit of each table entry.
- For one-hot equations, OR together the enabled incoming transitions.
- Treat a full question + submitted answer + success result as the required screenshot boundary.
