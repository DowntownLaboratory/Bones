# After you've connected over a serial connection, 
# we need to use these commands in the REPL to enable
# webrepl here: http://micropython.org/webrepl 

f = open('boot.py', 'w')
f.write("#boot (including wake-boot from deepsleep)\r\nimport uos, machine\r\nimport gc\r\nimport webrepl\r\n\r\n\r\ndef do_connect():\r\n\timport network\r\n\tsta_if = network.WLAN(network.STA_IF)\r\n\tif not sta_if.isconnected():\r\n\t\tprint(\'connecting to network...\')\r\n\t\tsta_if.active(True)\r\n\t\tsta_if.connect(\'Poop Lasagna 1\', \'Spring is finally here\')\r\n\t\twhile not sta_if.isconnected():\r\n\t\t\tpass\r\n\tprint(\'network config:\', sta_if.ifconfig())\r\n\r\ngc.collect()\r\ndo_connect()\r\nwebrepl.start()")
f.close()
import webrepl_setup
# Ctrl + D (Reboot)

# Alternatively you can enable the web repl without enabling wifi
# then you can copy over the boot.py script over the webrepl.
import webrepl
webrepl.start()
import webrepl_setup
# Ctrl + D (Reboot)