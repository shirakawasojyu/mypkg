import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

def cb(request, response):
    if request.name == "白川宗樹":
        response.age = 22
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)

pub = node.create_publisher(Person, "person", 10)
n = 0

def cb():
        global n
        msg = Person()
        msg.name = string
        msg.age = uint8
        pub.publish(msg)
        n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)
