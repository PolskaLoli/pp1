
a= input('enter washing product ')
b=input('rinse? true or false? ')
c=input('spin? true false? ')

time=0

if a=="underwear":
    time=time+70
    if b=="true":
        time=time+15
        if c=="true":
            time=time+9
        if c=="false":
            time=time+0
    if b=="false":
        time=time+0
        if c=="true":
            time=time+9
        if c=="false":
            time=time+0

if a=="jacket":
    time=time+40
    if b=="true":
        time=time+15
        if c=="true":
            time=time+9
        if c=="false":
            time=time+0
    if b=="false":
        time=time+0
        if c=="true":
            time=time+9
        if c=="false":
            time=time+0

if a=="shoes":
    time=time+20
    if b=="true":
        time=time+15
        if c=="true":
            time=time+9
        if c=="false":
            time=time+0
    if b=="false":
        time=time+0
        if c=="true":
            time=time+9
        if c=="false":
            time=time+0

print(time)











