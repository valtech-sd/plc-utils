import sys
from pylogix import PLC

# Check that argv[1] was passed and if not output with SYNTAX
script = sys.argv[0]
if len(sys.argv) < 4:
    print(f'SYNTAX: python ${script} <ip> <slot-no> <tag_name>')
    sys.exit(1)

ip = sys.argv[1]
slot = sys.argv[2]
tag_name = sys.argv[3]

with PLC() as comm:
    comm.IPAddress = ip
    comm.ProcessorSlot = int(slot)
    # read tag_name and set to variable
    response = comm.Read(tag_name)
    # check if the response contains the string Success
    if 'Success' in str(response):
        # get the value of the tag
        value = response.Value
        # print the value of the tag
        print(value)
    else:
        # print the string "error" and then the response
        print('ERROR: ' + str(response))



