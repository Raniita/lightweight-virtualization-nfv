from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink

def limit_perfTest():
    net = Mininet()
    h1 = net.addHost('h1')
    
    # Limit CPU at 20%
    h2 = net.addHost('h2', cls=CPULimitedHost, cpu=0.2)
    s1 = net.addSwitch('s1')
    c0 = net.addController('c0')
    
    # Limit BW 10mbps & delay 50ms
    net.addLink(h1,s1, cls=TCLink, bw=10, delay='50ms')
    net.addLink(h2,s1)
    net.start()
    CLI(net)
    net.stop()
    
if __name__ == '__main__':
    setLogLevel('info')
    limit_perfTest()
