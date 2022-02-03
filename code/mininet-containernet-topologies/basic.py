from mininet.net import Mininet
from mininet.topo import Topo

topo = Topo()				# Empty topology
topo.addSwitch("s1")		# Adding switch
topo.addHost("h1")			# Add Host
topo.addHost("h2")			# Add Host
topo.addLink("h1", "s1")	# Link host to switch
topo.addLink("h2", "s1")

net = Mininet(topo)			# Start Mininet
net.start()
net.pingAll()
net.iperf()
net.stop()
