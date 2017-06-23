
from heketi import HeketiClient
import sys
import json

xw = open("test.out", 'w')

client= HeketiClient('http://heketi-storage-project.cloudapps.mystorage.com','admin', 'My Secret')

c = client.cluster_list()
a = c.get('clusters')

for i in a:
    client.cluster_info(i)
    xw.write('Heketi Cluster information for Id {} Begins \n'.format(i))
    b = client.cluster_info(i)
    cluster_info = json.dumps(b, indent=4, sort_keys=True)
    xw.write(cluster_info + "\n\n" )
    f = b.get('nodes')
    g = b.get('volumes')

    xw.write('\n\n\n\n')
    xw.write('Node Information for the Cluster Begins \n\n')

    for i in f:
        client.node_info(i)
        xw.write('Node Info for Id {} is \n'.format(i))
        cni = client.node_info(i)
        node_info = json.dumps(cni, indent=4, sort_keys=True)
        xw.write(node_info + "\n\n")

    xw.write('\n\n\n\n')
    xw.write('Volume Information for the Cluster Begins \n\n')

    for i in g:
        client.volume_info(i)
        xw.write('Volume Info for Id {} is \n'.format(i))
        cvi = client.volume_info(i)
        volume_info = json.dumps(cvi, indent=4, sort_keys=True)
        xw.write(volume_info + "\n\n")

xw.close()
