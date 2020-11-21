import time 
from umqtt.simple import MQTTClient

def main(server="localhost"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    n = 0
    while n < 100:
        msg = b"hello: %d" % (n)
        print('published message', msg)
        c.publish(b"test", msg)
        n = n + 1
        
        time.sleep(1)
    c.disconnect()


if __name__ == "__main__":
    main("192.168.0.206")