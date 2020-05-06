
import camelcase
C = camelcase.CamelCase()
Message = "i am feeling lucky"
print(Message)
newMsg = C.hump(Message)
print(newMsg)