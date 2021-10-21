# Ejemplo práctico entorno de pruebas usando ns y ovs
## Comandos utilizados

1. `ip netns add h1`
2. `ip netns add h2`
3. `ip netns exec h1 bash` (en una nueva terminal que llamo h1)
4. `ip netns exec h2 bash` (en una nueva terminal que llamo h2)
5. `ovs-vsctl add-br s1`
6. `ip link add h1-eth0 type veth peer name s1-eth1`
7. `ip link add h2-eth0 type veth peer name s1-eth2`
8. `ip link set h1-eth0 netns h1`
9. `ip link set h2-eth0 netns h2`
10. `ovs-vsctl add-port s1 s1-eth1`
11. `ovs-vsctl add-port s1 s1-eth2`
12. `ovs-vsctl show`
13. (en h1) `ifconfig h1-eth0 10.0.0.1` # o en la terminal
14. (en h1) `ifconfig lo up`
15. (en h2) `ifconfig h2-eth0 10.0.0.2`
16. (en h2) `ifconfig lo up`
17. `ifconfig s1-eth1 up`
18. `ifconfig s1-eth2 up`
19. `ovs-ofctl add-flow s1 in_port=1,actions=output:2`
20. `ovs-ofctl add-flow s1 in_port=2,actions=output:1`
21. (en h1) `ping -c4 10.0.0.2`
22. Undo everything
23. `ovs-vsctl del-br s1`
24. `ip link delete s1-eth1`
25. `ip link delete s1-eth2`
26. `ip netns del h1`
27. `ip netns del h2`


## Comentarios
`lsns` solo muestra los ns con al menos una aplicación asociada, pero no
los definidos "a medio gas". Sin embargo ip netns list muestra los
net-ns (incluidos los "a medio gas")

Para que el openvswitch funcione, el sistema debe haber arrancado su
demonio asociado. Lo más facil es hacer:
`systemctl start openvswitch.service`
`systemctl enable openvswitch.service` (hace el cambio permanente)

Si queréis que el switch se comporte como un Learning-switch normal y
corriente:
`ovs-vsctl set-controller s1 ptcp:127.0.0.1`
`ovs-testcontroller ptcp: &` (en ubuntu creo que es ovs-controller)

### Ejemplo con unshare:
#### Namespace UTS 
* `unshare --uts /bin/bash`
* `hostname prueba`
* `hostname` # en las dos terminales
* `exit` destruye el ns

#### Namespace mount
* `mkdir /tmp/prueba`
* `unshare --mount /bin/bash`
* `mount -n -t tmpfs tmpfs /tmp/prueba`
* `df -h` en ambos terminales

#### Namespace netns
* `unshare --net /bin/bash`
* `ifconfig` en ambos terminales
* `exit`

Con varios ns de diferente tipo
* `unshare --net --mount --uts /bin/bash`

### Namespaces pesistentes
Para que un namespace permanezcan después del exit, y retomarlos con un nsenter (es
decir, cómo crear un ns "a medio gas" y añadirle una app cuando quiera
con nsenter)
* `touch /root/ns-uts`
* `unshare --uts=/root/ns-uts`
* `hostname FooBar`
* `exit`
* `nsenter --uts=/root/ns-uts /bin/bash`
* `hostname`
* `exit`
* `umount /root/ns-uts # esto mata el ns definitivamente`

El netns no tiene nombre cuando se crea con unshare ¿cómo arreglarlo?
en `/var/run/netns/`, ejecutando `ln -s /proc/<pid>/ns/net h1`

### Recordatorio
Un netns creado con el comando ip crea automáticamente un
mount-ns con TODOS los archivos de configuración de red INDEPENDIENTES
del sistema. Con el unshare, habría que crear dos ns (uno de net y otro
de mount) y en el de mount poner los archivos de configuración.
