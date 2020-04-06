''' This program will have some functions to help parsing the bitcoin blockchain'''


'''

Function 1:- Input is a blkxxxx.dat file
             Output is an list of the form: [ [block a], [block c], [block b],..., [block n]]
                where [block x] of the form ['byte0','byte1','byte2', ... ,'byten'] (where bytes ARE in order)

Note:- the output list of blocks is NOT necessarily in order block 1,2,3 etc. since they are downloaded in any order from bitcoin core


'''

def parsefile(filepath):


   #Open the blk file as 'read binary'
   f=open(filepath,"rb")
   reading = f.read()

   #name some variables we will use in the loop, counter is a parameter that will be used to count each byte in the file sequentially, j is to count the total number of blocks, blocks is the initial empty list
   counter = 0
   j=0
   blocks = []
   magic = ['0xf9', '0xbe', '0xb4', '0xd9']


   #make a while loop to loop through the file and add each block to the list separately, while TO 300000 is arbitrary large number
   while j<300000:

      #Check the first 4 bytes are magic
      check = []
      try:
         for i in range(counter, counter+4):
            check.append(hex(reading[i]))
            #print(hex(reading[i]))

      except Exception as e:
         print(e)
         break

      #create the first part of the block
      block = check


      #add 4 to the counter, so we can look at the next element
      counter = counter + 4

      #Get the size of the block, blocksize max is fixed
      size = []
      for i in range(counter, counter +4):
         size.append(hex(reading[i]))
         #print(hex(reading[i]))
      size_int = int(size[3], 0)*16**6+int(size[2], 0)*16**4+int(size[1], 0)*16**2+int(size[0], 0)*16**0

      #add 4 to the counter, so we can look at the next element
      counter = counter + 4

      #Now we have the second element of the block add it to the block
      block = block + size

      #now we know the network magic was ok, and we know the size of the block, we can add the block bytes to the array
      for i in range(counter, counter + size_int):
         block.append(hex(reading[i]))

      #add the block to the blocks list
      blocks.append(block)

      #add the size of the block to the counter so we can move on to the next block
      counter = counter + size_int

      j=j+1

   #close the file
   f.close()
   return blocks




'''

Function 2:- Parse a block into simple JSON string

Parse the specified block to get in the form:

Network Magic
Block size
Block Header
Number of Transactions
Transactions

'''

def parseblock(blocks):
   blocks2 = []
   for i in range(len(blocks)):
      block = blocks[i]
      block_update = []

      block_update = [block[0:4],block[4:8],block[8:12],block[12:44],block[44:76],block[76:80],block[80:84],block[84:88],block[88:]]

      blocks2.append(block_update)

   return blocks2
