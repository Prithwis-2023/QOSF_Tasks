from qiskit import QuantumCircuit, QuantumRegister

qr = QuantumRegister(3)
qc = QuantumCircuit(qr)
qc.xor(qr[0])
print(qc.decompose().draw())
