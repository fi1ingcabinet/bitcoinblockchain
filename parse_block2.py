
def parseblock(blocks):


   blocks2 = []
   for i in range(len(blocks)):
      block = blocks[i]
      block_update = []

      block_update = [block[0:4],block[4:8],block[8:12],block[12:44],block[44:76],block[76:80],block[80:84],block[84:88],block[88:]]
      
      blocks2.append(block_update)

   return blocks2
