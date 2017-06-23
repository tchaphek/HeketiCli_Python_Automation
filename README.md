# HeketiCli_Python_Automation

Heketi

Heketi provides a RESTful management interface which can be used to manage the life cycle of GlusterFS volumes. With Heketi, cloud services like OpenStack Manila, Kubernetes, and OpenShift can dynamically provision GlusterFS volumes with any of the supported durability types. Heketi will automatically determine the location for bricks across the cluster, making sure to place bricks and its replicas across different failure domains. Heketi also supports any number of GlusterFS clusters, allowing cloud services to provide network file storage without being limited to a single GlusterFS cluster.


Heketi- Client For Python

The Heketi-Client for Python uses API to interact with various components of Heketi-Cli, the scripts as a part of this repo are meant to automated basic operations using Heketi Python Client

Following are the operations currently supported for automation

1. Gathering the Cluster, Node, Volume and Brick Information after the installation is successfully complete.
2. Performing a Device add to the nodes and verifying its success
2. Gathering information on the newly added device
4. Performing a Device Removal on the newly added devices with no bricks attached to them.
