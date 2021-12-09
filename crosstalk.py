import numpy as np
import pdb
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# from ibm_quantum_widgets import *
from qiskit.providers.aer import QasmSimulator
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi
import numpy as np
from numpy import mean
from qiskit.tools.monitor import job_monitor
from qiskit import execute

# Loading your IBM Quantum account(s)

provider = IBMQ.save_account('b7bba0d40e6634300191a9b19841070686130b6652f2e566ef2ef7b704ea6a6885a6855c32875ee1124093358514a3408926b17e3b793445040ac922ac65ffc1')
provider = IBMQ.load_account()
provider2 = IBMQ.get_provider(hub='ibm-q-pnnl', group='internal', project='default')
print(provider2.backends())
mybackend = provider2.get_backend('ibmq_casablanca')
def btest( list ):
    q = QuantumRegister(6, 'q')
    c = ClassicalRegister(6, 'c')
    circuit2 = QuantumCircuit(q, c)
    circuit2.x(q[list[0]])
    circuit2.x(q[list[2]])
    circuit2.cx(q[list[0]], q[list[1]])
    circuit2.barrier()
    circuit2.cx(q[list[2]], [list[3]])
    circuit2.measure(q[list[0]],c[list[0]])
    circuit2.measure(q[list[1]],c[list[1]])
    circuit2.measure(q[list[2]],c[list[2]])
    circuit2.measure(q[list[3]],c[list[3]])
    #circuit2.draw(output = 'mpl')
    shots = 20000
    string = "000000"

    for i in list:
        string = string[:i] + '1' + string[i + 1:]

    string = string[::-1]
    print(string)
    
    job_exp = execute(circuit2, mybackend, shots=shots, initial_layout=[0, 1, 2,3,4,5])
    job_monitor(job_exp)
    result = job_exp.result()
    counts = result.get_counts()
    error_rate = 1-counts[string] / shots
    return error_rate
def ctest( list ):
    q = QuantumRegister(6, 'q')
    c = ClassicalRegister(6, 'c')
    circuit2 = QuantumCircuit(q, c)
    circuit2.x(q[list[0]])
    circuit2.x(q[list[2]])
    circuit2.cx(q[list[2]], q[list[1]])
    circuit2.cx(q[list[0]], q[list[1]])
    # circuit2.barrier(q[list[0]])
    # circuit2.barrier(q[list[1]])
    # circuit2.barrier(q[list[2]])
    # circuit2.barrier(q[list[3]])
 
    circuit2.cx(q[list[2]], [list[3]])
    circuit2.measure(q[list[0]],c[list[0]])
    circuit2.measure(q[list[1]],c[list[1]])
    circuit2.measure(q[list[2]],c[list[2]])
    circuit2.measure(q[list[3]],c[list[3]])
    #circuit2.draw(output = 'mpl')
    string = "000000"
    shots = 20000
    for i in list:
        string = string[:i] + '1' + string[i + 1:]

    string = string[::-1]
    print(string)
    
    job_exp = execute(circuit2, mybackend, shots=shots, initial_layout=[0, 1, 2,3,4,5])
    job_monitor(job_exp)
    result = job_exp.result()
    counts = result.get_counts()
    error_rate = 1-counts[string] / shots
    return error_rate

testlist = [1,2,3,5]
cross = []
for x in range(10):
    cur = ctest(testlist) 
    cross.append(cur)
    print(cur)
print(cross)
# print("with crosstalk error")
# print(mean(nocross))
crosserror = mean(cross)
print(crosserror)

nocross = []
for x in range(10):
    cur = btest(testlist) 
    nocross.append(cur)
    print(cur)
print(nocross)
# print("with crosstalk error")
# print(mean(nocross))
nocrosserror = mean(nocross)
print(nocrosserror)
print("with crosstalk error")
print(crosserror)
print("without crosstalk error")
print(nocrosserror)