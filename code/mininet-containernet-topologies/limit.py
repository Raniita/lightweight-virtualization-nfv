from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink

def limit_perfTest():
    net = Mininet()
    
    # Host 1: CPU at 10%
    h1 = net.addHost('h1', cls=CPULimitedHost, cpu=0.1)		
    h2 = net.addHost('h2')
    
    s1 = net.addSwitch('s1')
    c0 = net.addController('c0')
    
    # Link h1<->s1: BW 5mbps & delay 80ms
    net.addLink(h1,s1, cls=TCLink, bw=5, delay='80ms')
    net.addLink(h2,s1)
    
    net.start()
    net.pingAll()
    net.iperf()
    CLI(net)
    net.stop()
    
if __name__ == '__main__':
    setLogLevel('info')
    limit_perfTest()
