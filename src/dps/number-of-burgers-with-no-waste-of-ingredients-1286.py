class Solution:
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        '''
        for jumbo in range(cheeseSlices + 1):
            small = cheeseSlices - jumbo
            
            if small * 2 + jumbo * 4 == tomatoSlices:
                return [small, jumbo]
        return []
        '''
        jumbo = (tomatoSlices - 2 * cheeseSlices) / 2
        small = cheeseSlices - jumbo

        if int(jumbo) == jumbo and int(small) == small and jumbo >= 0 and small >= 0:
            return [int(jumbo), int(small)]
        return []