import matplotlib.pyplot as plt
import numpy as np
import math
from math import pi
import cmath
from qiskit import QuantumCircuit, QuantumRegister, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.circuit import Gate
from qiskit.extensions import UnitaryGate

#Decomposition of the U and CX to create the CCX gate

#Defining the gate V such that V^2 = X.
qubits = QuantumRegister(1)
qc0 = QuantumCircuit(qubits)
qc0.u(pi/2, -pi/2, pi/2, qubits)
sx_gate = qc0.to_gate().control(1)

#Defining the conjugate transpose of V
qc1 = QuantumCircuit(qubits)
qc1.u(-pi/2, -pi/2, pi/2, qubits)
sxdg_gate =qc1.to_gate().control(1)

#Defining the primary quantum circuit for ccx
qubits_circuit0 = QuantumRegister(3)
qc2 = QuantumCircuit(qubits_circuit0)
qc2.append(sx_gate, [qubits_circuit0[1], qubits_circuit0[2]])
qc2.cx(qubits_circuit0[0], qubits_circuit0[1])
qc2.append(sxdg_gate, [qubits_circuit0[1], qubits_circuit0[2]])
qc2.cx(qubits_circuit0[0], qubits_circuit0[1])
qc2.append(sx_gate, [qubits_circuit0[0], qubits_circuit0[2]])

#Drawing the ccx circuit
print(qc2.draw())

#Decomposition of the U and CX to create the CCCX gate

#Defining the gate V such that V^4 = X.
qc3 = QuantumCircuit(qubits)
qc3.u(pi/4, -pi/2, pi/2, qubits)
fourth_x_gate = qc3.to_gate().control(1)

#Defining the conjugate transpose of V
qc4 = QuantumCircuit(qubits)
qc4.u(-pi/4, -pi/2, pi/2, qubits)
fourth_x_gatedg =qc4.to_gate().control(1)

#Defining the primary quantum circuit for cccx
qubits_circuit1 = QuantumRegister(4)
qc5 = QuantumCircuit(qubits_circuit1)
qc5.append(fourth_x_gate, [qubits_circuit1[0], qubits_circuit1[3]])
qc5.cx(qubits_circuit1[0], qubits_circuit1[1])
qc5.append(fourth_x_gatedg, [qubits_circuit1[1], qubits_circuit1[3]])
qc5.cx(qubits_circuit1[0], qubits_circuit1[1])
qc5.append(fourth_x_gate, [qubits_circuit1[1], qubits_circuit1[3]])
qc5.cx(qubits_circuit1[1], qubits_circuit1[2])
qc5.append(fourth_x_gatedg, [qubits_circuit1[2], qubits_circuit1[3]])
qc5.cx(qubits_circuit1[0], qubits_circuit1[2])
qc5.append(fourth_x_gate, [qubits_circuit1[2], qubits_circuit1[3]])
qc5.cx(qubits_circuit1[1], qubits_circuit1[2])
qc5.append(fourth_x_gatedg, [qubits_circuit1[2], qubits_circuit1[3]])
qc5.cx(qubits_circuit1[0], qubits_circuit1[2])
qc5.append(fourth_x_gate, [qubits_circuit1[2], qubits_circuit1[3]])

#Drawing the cccx circuit
print(qc5.draw())





