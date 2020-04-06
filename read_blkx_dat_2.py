#asdf
def parsefile():
   #Open the blk file

   f=open("/var/tmp/blkchn/blk00000.dat","rb")

   reading = f.read()

   counter = 0

   j=0

   blocks = []

   while j<300000:

      #Check the first 4 bytes are magic

      magic = ['0xf9', '0xbe', '0xb4', '0xd9']
      check = []
      try:
         for i in range(counter, counter+4):
            check.append(hex(reading[i]))
            #print(hex(reading[i]))

         #print(magic==check)
      except Exception as e:
         print(e)
         break
      

      counter = counter + 4

      #If true get the size of the block

      size = []
      for i in range(counter, counter +4):
         size.append(hex(reading[i]))
         #print(hex(reading[i]))
      size_int = int(size[3], 0)*16**6+int(size[2], 0)*16**4+int(size[1], 0)*16**2+int(size[0], 0)*16**0

      counter = counter + 4

      #print("size: ", size_int)

      block = check + size
      for i in range(counter, counter + size_int):
         block.append(hex(reading[i]))

      blocks.append(block)
      #print(block)

      counter = counter + size_int

      #print(counter)
      #if size_int!=215 and size_int!=216:
         #print(block)
      #print(j)
      j=j+1

      #print(blocks)

   f.close()
   return blocks
