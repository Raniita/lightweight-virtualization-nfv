# TUN/TAP Tests

* Utilizamos el archivo ``tuntap.c''
* Compilamos con gcc: ``gcc tun.c -o tun''
* Ejecutamos el programa, este se quedará "bloqueado", pero se habrá creado la interfaz __tun0__
* En otra terminal, ejecutamos los siguientes comandos:
``
> ip address {buscamos la interfaz tun0}
> ip addr add 192.168.209.138/24 dev tun0
> ip link set dev tun0 up
``
* En otra terminal, dejamos ejecutando tcpdump -i tun0 [mantenemos a la escucha]
* Ahora, realizamos un ping a cualquier IP dentro del rango asignado:
``
> ping -c 4 192.168.209.139 -I tun0
``

* En la ventana del tcpdump nos debería aparecer las capturas de los diferentes paquetes.
* En la ventana del ping, no veremos respuesta alguna ya que no hacemos nada al recibir los paquetes de datos en el programa, por lo tanto equivale a paquete descartado. El programa ping no recibe callback, aunque en el resto de terminales si veremos como si hemos recibido información.

## Referencias
[Github: simpletun.c](https://github.com/gregnietsky/simpletun/blob/master/simpletun.c)
[Principio de diseño del controlador TUN/TAP de la tarjeta de red virtual](https://programmerclick.com/article/45831226469/)
[Controlador de dispositivo TUN/TAP del kernel de Linux](https://programmerclick.com/article/3312224272/)
