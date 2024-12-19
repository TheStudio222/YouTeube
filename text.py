import uuid
uuid.uuid4()
import random
while True:
    id = str(uuid.uuid4())
    trimmed = id[:random.randint(0,len(id)-1)]
    spaces = " " * random.randint(0,100)
    print(f"{spaces}{trimmed}")