one=open ('meatandfish.txt ','r')
two=open ('grainsandbread.txt ','r')

three=open('allproduct','w')

read1=one.read()
read2=two.read()

three.write(read1)
three.write(read2)

one.close()
two.close()
three.close()
