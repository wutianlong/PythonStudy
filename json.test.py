import json

data = {"a":1,"b":2,"c":3}

jsonValue = json.dumps(data)
print ("jsonValue = %s" % jsonValue )


pythonValue = json.loads(jsonValue)
print("pythonValue =  %s " % pythonValue )

