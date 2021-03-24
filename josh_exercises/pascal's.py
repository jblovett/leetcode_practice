class Solution:
    """A simple class for the leetcode Pascal solution"""
    def pascals(self, k: int) -> list:
        """returns the kth row of Pascal's Triangle, where the first row is 0"""
        array1 = [1, 1]
        if (k < 0):
            raise ValueError(k)
        if (k == 0):
            array0 = [1]
            return array0
        elif (k == 1):
            return array1
        else:
            row_counter = 1        
            while row_counter != k:
                i = 0
                array2 = [0] * (len(array1) + 1)  
                while i <= len(array1):
                    print("nested")
                    if i == 0:
                        array2[i] = array1[i]
                    elif i == len(array1):
                        array2[i] = array1[i - 1]
                    else:
                        array2[i] = (array1[i-1] + array1[i])
                    i = i + 1
                row_counter = row_counter + 1
                print("main")
                if row_counter < k:
                    array1 = array2
            return array2


def main() -> None:
    a = Solution()
    print(str(a.pascals(3)))


          

if __name__ == "__main__":
    main()