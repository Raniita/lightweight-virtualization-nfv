# Working with network namespaces on Linux (and OpenFlow)
## Beginner tutorial
### Commands
Creating the namespaces
* `ip netns add h1`
* `ip netns add h2`
* `ip netns exec h1 /bin/bash ` [on a terminal for h1]
* `ip netns exec h2 /bin/bash ` [on a terminal for h2]

Create bridge interface and assign to openflow
* `ovs-vsctl add-br s1`
* `ip link add h1-eth0 type veth peer name s1-eth1`
* `ip link add h2-eth0 type veth peer name s1-eth2`
* `ip link set h1-eth0 netns h1`
* `ip link set h2-eth0 netns h2`
* `ovs-vsctl add-port s1 s1-eth1`
* `ovs-vsctl add-port s1 s1-eth2`
* `ovs-vsctl show`

Enable interfaces
* `h1> ifconfig h1-eth0 10.0.0.1`
* `h1> ifconfig lo up`
* `h2> ifconfig h2-eth0 10.0.0.2`
* `h2> ifconfig lo up`
* `ifconfig s1-eth1 up`
* `ifconfig s1-eth2 up`

Openflow routing
* `ovs-ofctl add-flow s1 in_port=1,actions=output:2`
* `ovs-ofctl add-flow s1 in_port=2,actions=output:1`
* `h1> ping -c4 10.0.0.2`

### Undo everything
* exit on each /bin/bash netns
* `ovs-vsctl del-br s1`
* `ip link delete s1-eth1`
* `ip link delete s1-eth2`
* `ip netns del h1`
* `ip netns del h2`
