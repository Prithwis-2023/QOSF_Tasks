from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import HGate

qr = QuantumRegister(2)
qc = QuantumCircuit(qr)
c3h_gate = HGate().control(1)
qc.append(c3h_gate, qr)
print(qc.draw())

qc2 = QuantumCircuit(3)
qc2.append(c3h_gate, [0, 1])
print(qc2.draw())