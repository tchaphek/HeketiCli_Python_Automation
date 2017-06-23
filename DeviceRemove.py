from heketi import HeketiClient
import sys
import json

xw = open("nodes.out", 'w')
node_output = open("node_output", "w")

client= HeketiClient('http://heketi-storage-project.cloudapps.mystorage.com','admin', 'My Secret')

c = client.cluster_list()
a = c.get('clusters')

for i in a:
    client.cluster_info(i)
    b = client.cluster_info(i)
    f = b.get('nodes')
    g = f[1]

cni = client.node_info(g)
node_info = json.dumps(cni, indent=4, sort_keys=True)
xw.write(node_info)

xw.close()

json_file = open ("nodes.out")
json_data = json.load(json_file)
global name,state,deviceId
for device in json_data['devices']:
    name = device['name']
    state = device['state']
    deviceId = device['id']
    if name == '/dev/sde':
        di = client.device_info(deviceId)
        devinfo = json.dumps(di, indent=4, sort_keys=True)
        node_output.write(devinfo)
        node_output.write('\n')
        client.device_delete(deviceId)
        node_output.write("The device Name {} with Id {} is deleted successfully \n".format(name, deviceId))
        node_output.write('\n')


