import base64

def encode_(msg):
    en = msg.encode("ascii")
    enco = base64.b64encode(en)
    return enco


mail = "yusufakdo.47@gmail.com"
passw = ""

print(encode_(mail), encode_(passw))