# Evan Pendergraft
# CITA 180_0W1_BURL - Intro to Programming (Spring 2024)
# Programming Assignment 05

# Input -- keep the following entries -- you may add others for testing
portSummary = ("1-11 untagged", "12 excluded")
# portSummary = ("1-6 untagged", "7 excluded", "8-12 untagged")

# Processing (Your Code goes here
port_details = []
for grouping in portSummary:
    port_range_string = grouping.split()[0]
    port_state = grouping.split()[1]
    port_range = []

    for port_string in port_range_string.split("-"):
        port_int = int(port_string)
        port_range.append(port_int)

    if len(port_range) != 2:
        port_details.append('{:>2}: {}'.format(port_range_string, port_state))
    else:
        for port in range(port_range[0], port_range[1] + 1):
            port_details.append('{:>2}: {}'.format(port, port_state))

# Output -- Do not change any of the code in Output
print("Port Details")
for port in port_details:
    print(port)
