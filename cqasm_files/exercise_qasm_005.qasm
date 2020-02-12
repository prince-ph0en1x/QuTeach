version 1.0
# this file has been automatically generated by the OpenQL compiler please do not modify it manually.
qubits 7

.initialize
    prep_z q[0]
    prep_z q[1]
    prep_z q[2]
    prep_z q[3]
    prep_z q[4]
    prep_z q[5]
    prep_z q[6]
    x q[2]
    x q[4]
    display

.adder
    toffoli q[1],q[2],q[3]
    cnot q[1],q[2]
    toffoli q[0],q[2],q[3]
    toffoli q[4],q[5],q[6]
    cnot q[4],q[5]
    toffoli q[3],q[5],q[6]
    cnot q[4],q[5]
    cnot q[4],q[5]
    cnot q[3],q[5]
    toffoli q[0],q[2],q[3]
    cnot q[1],q[2]
    toffoli q[1],q[2],q[3]
    cnot q[1],q[2]
    cnot q[0],q[2]
    display
