import sys
from pylogix import PLC

# Check to ensure we were passed the 2 arguments we need.
script = sys.argv[0]
if len(sys.argv) < 3:
    print(f"SYNTAX: python ${script} <ip> <slot-no>")
    sys.exit(1)

ip = sys.argv[1]
slot = int(sys.argv[2])

with PLC() as comm:
    # '172.20.72.3'
    comm.IPAddress = ip
    if slot > 0:
        comm.ProcessorSlot = slot
    print("comm = " + str(comm))
    try:
        tags = comm.GetTagList()
    except Exception as e:
        # TODO: This does not catch on PLC TIMEOUT. How to catch failures to connect?
        print("Failed to establish a connection to the PLC. Exception: {}".format(e))
        tags = None
    if tags is not None:
        for t in tags.Value:
            print(t.TagName, t.DataType)
