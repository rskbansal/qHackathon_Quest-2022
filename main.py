# Importing required libraries
import numpy as np

# Defining Basis Vectors of Single-Qubit system
q0 = np.array([[1], [0]])
q1 = np.array([[0], [1]])

# Defining Gates
X_gate = np.array([[0, 1], [1, 0]])
Y_gate = np.array([[0, -1j], [1j, 0]])
Z_gate = np.array([[1, 0], [0, -1]])
H_gate = np.array([[1, 1], [1, -1]])*(1/np.sqrt(2))
CNOT_gate = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# Mapping Gates 
gates = {
    "X":X_gate, 
    "Y":Y_gate, 
    "Z":Z_gate, 
    "H":H_gate, 
    "CNOT":CNOT_gate, 
}

# Mapping Qubits
qubits = {
    'Q0':q0,
    'Q1':q1,
    'Q0Q0':np.kron(q0,q0),
    'Q0Q1':np.kron(q0,q1),
    'Q1Q0':np.kron(q1,q0),
    'Q1Q1':np.kron(q1,q1)
}

while True:
    # MENU
    print('Menu') 
    print('----------------------------------------------------')
    print('Q0 for initializing normalized Q0 Qubit') 
    print('Q1 for initializing normalized Q1 Qubit') 
    print('GATE [GATE] for displaying gate matrix')
    print('OP [GATE]|[QUBIT(S)]> for applying Gates on Qubit(s)')
    print('EXIT to exit')

    # Taking Input
    option = input("Enter choice : ")

    if(option=='Q0'):
        q0_0 = int(input())
        q0_1 = int(input())
        q0 = np.array([[q0_0], [q0_1]])
        print(q0)

    if(option=='Q1'):
        q1_0 = int(input())
        q1_1 = int(input())
        q1 = np.array([[q1_0], [q1_1]])
        print(q1)

    if(option.split(' ')[0]=='GATE'):
        print(gates[option.split(' ')[1]])

    if(option.split(' ')[0]=='OP'):
        # Breaking the input to extract useful info
        string_part = option.split(' ')[1].partition('|')
        gate = gates[string_part[0].upper()]
        qubit = qubits[string_part[2][:-1]]

        print(np.matmul(gate, qubit))

    if(option=='EXIT'):
        break

    else:
        continue

