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

t = (0, 1, 2, 3)
t = list(t)
t_ = sorted(t, reverse=True)
qr = QuantumRegister(5)
qc = QuantumCircuit(qr)

length = len(t_)
target =t_[0]
for ele in t_[1:]:
    qc.cx(qr[ele], qr[target])

print(qc.draw())