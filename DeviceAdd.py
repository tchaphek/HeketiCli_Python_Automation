from heketi import HeketiClient
import sys
import json

Device_Add = open("deviceadd.out", 'w')

client= HeketiClient('http://heketi-storage-project.cloudapps.mystorage.com','admin', 'My Secret')

c = client.cluster_list()
a = c.get('clusters')

for i in a:
    client.cluster_info(i)
    b = client.cluster_info(i)
    f = b.get('nodes')
    node_info = json.dumps(f, indent=4, sort_keys=True)
    Device_Add.write('Heketi Cluster Node information is \n\n')
    Device_Add.write(node_info + "\n\n" )

    for i in f:
        client.device_add(device_options={"node": i, "name": "/dev/sde"})
        Device_Add.write('Device Add Successful for Node {}\n'.format(i))
