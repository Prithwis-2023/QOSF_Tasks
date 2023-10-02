import matplotlib.pyplot as plt
import numpy as np
import math
from math import pi
import cmath
import itertools
from qiskit import QuantumCircuit, QuantumRegister, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.circuit import Gate
from qiskit.extensions import UnitaryGate

n = int(input("Enter the number of qubits for the circuit: "))

qr0 = QuantumRegister(1)
qc0 = QuantumCircuit(qr0, name='V')
k = 2**(n-2)
qc0.u(pi/k, -pi/2, pi/2, qr0)
v_gate = qc0.to_gate().control(1)

qc1 = QuantumCircuit(qr0, name='V_dag')
qc1.u(-pi/k, -pi/2, pi/2, qr0)
vdg_gate = qc1.to_gate().control(1)


qr = QuantumRegister(n)
qc = QuantumCircuit(qr)

def gate(t):
    t =list(t)
    t_ = sorted(t, reverse=True)
    length = len(t_)
    target = t_[0]
    for ele in t_[1:]:
        qc.cx(qr[ele], qr[target])

def multicontrolled(qubits):
    l =[]
    for i in range(qubits-1):
        l.append(i)
    target = qubits - 1
    for ele in l:
        qc.append(v_gate, [qr[ele], qr[target]])    
    qc.barrier()

    for i in range(2, qubits):
        combs = list(itertools.combinations(l, i))
        for comb in combs:
            #print(comb)
            gate(comb)
            if len(comb) % 2 == 0:
                qc.append(vdg_gate, [qr[comb[-1]], qr[target]])
            elif len(comb) % 2 != 0:
               qc.append(v_gate, [qr[comb[-1]], qr[target]]) 
            gate(comb)
            qc.barrier()
    print(qc.draw())

multicontrolled(n)
        