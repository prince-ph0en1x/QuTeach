# Quantum Search

from openql import openql as ql
import os

curdir = os.path.dirname(__file__)
output_dir = os.path.join(curdir, 'cqasm_files')
ql.set_option('output_dir', output_dir)
ql.set_option('write_qasm_files', 'yes')

config_fn  = os.path.join(curdir, 'config_qx.json')
platform   = ql.Platform('platform_none', config_fn)

num_qubits = 9
p = ql.Program('exercise_qasm_008', platform, num_qubits)

k1 = ql.Kernel("initialize", platform, num_qubits)
for i in range(0, num_qubits):
	k1.gate('prep_z', [i])	# Initialize all qubits to |0>
k1.gate('rx', [0], 0, 1.3)	# Create a arbitrary state
k1.gate('ry', [0], 0, 0.3)	# Create a arbitrary state
k1.display()
p.add_kernel(k1)

k2 = ql.Kernel("phase_encode", platform, num_qubits)
k2.gate('x', [2])
    # cnot q0,q3
    # cnot q0,q6
    # h q0
    # h q3
    # h q6
k2.display()
p.add_kernel(k2)

k3 = ql.Kernel("bitflip_encode", platform, num_qubits)
	# cnot q0,q1
 #    cnot q0,q2
 #    cnot q3,q4
 #    cnot q3,q5
 #    cnot q6,q7
 #    cnot q6,q8
k3.display()
p.add_kernel(k3)

k4 = ql.Kernel("inject_error", platform, num_qubits)
    # x q0
    # z q0
    # x q1
k4.display()
p.add_kernel(k4)

k5 = ql.Kernel("bitflip_decode_and_correct", platform, num_qubits)
    # cnot q0,q1
    # cnot q0,q2
    # toffoli q2,q1,q0
    # cnot q3,q4
    # cnot q3,q5
    # toffoli q5,q4,q3
    # cnot q6,q7
    # cnot q6,q8
    # toffoli q8,q7,q6
k5.display()
p.add_kernel(k5)

k6 = ql.Kernel("phaseflip_decode_and_correct", platform, num_qubits)
    # h q0
    # h q3
    # h q6
    # cnot q0,q3
    # cnot q0,q6
    # toffoli q6,q3,q0
k6.display()
p.add_kernel(k6)

p.compile()

qasm = p.qasm()			# Get the cqasm generated by OpenQL
print(qasm)