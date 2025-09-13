import lab_chat as lc
from lab_chat import join_group


def get_username():
    username=input("enter username:")
    return username.strip().upper()

def get_group():
    group=input("enter group name:")
    return group.strip().upper()

def get_message():
    message=input("awaiting message:")
    return message.strip()

def initialize_chat():
    temp_username = get_username()
    temp_group = get_group()
    temp_n = lc.get_peer_node(temp_username)
    lc.join_group(temp_n, temp_group)
    chan = lc.get_channel(temp_n,temp_group)
    return chan

def start_chat():
    channel = initialize_chat()
    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("sent")

print(type(initialize_chat()))

start_chat()
#print(get_username())
#print (get_group())
#initialize_chat()
