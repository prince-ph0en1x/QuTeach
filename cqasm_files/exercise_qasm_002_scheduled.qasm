version 1.0
# this file has been automatically generated by the OpenQL compiler please do not modify it manually.
qubits 2
.entangle

    prep_z q[0]
    wait 1
    { prep_z q[1] | h q[0] }
    wait 1
    cnot q[0],q[1]
    wait 3
    { display | measure q[0] | measure q[1] }
    wait 14
    display

