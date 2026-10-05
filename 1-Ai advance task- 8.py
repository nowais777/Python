log = "INFO:Server Started Successfully"

print("Partition:", log.partition(":"))
print("Split:", log.split(":"))

position = log.find(":")
print("Colon position:", position)

print("Using index:", log.index(":"))

level = log[:position]
message = log[position + 1:]

print("Level:", level)
print("Message:", message)