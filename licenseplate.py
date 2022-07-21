"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #9 - License Plate (licenseplate.py)


Author: Wonjun Lee

Difficulty Level: 5/10

Prompt: Jon was speeding on the highway with his RACECAR, and the highway camera has taken a picture 
of the RACECAR’s number plate. However, some characters on the plate are blurry. Please write a function 
that returns the number of possible combinations of the number plate. The number plate for his RACECAR
consists of 7 distinct characters, starting with 3 distinct alphabets and ending with 4 distinct numbers. 
The input will be passed as a string and any blurred characters will be written as ‘.’

Test Cases: 
Input: “ABC123.” ; Output: 7
Input: “.ON0123” ; Output: 24
Input: “.BC.234” ; Output: 168
"""

class Solution:
    def licensePlate(self,str):
        # type str: string
        # return: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        letters = str[:3]
        numbers = str[3:7]
        counter = 0
        poss = 1

        for i in letters:
            if i == ".":
                counter += 1
        
        if counter == 1:
            poss *= 24
        elif counter == 2:
            poss *= 25*24
        elif counter == 3:
            poss *= 26*25*24

        counter = 0

        for n in numbers:
            if n == ".":
                counter += 1
        
        if counter == 1:
            poss *= 7
        elif counter == 2:
            poss *= 8*7
        elif counter == 3:
            poss *= 9*8*7
        elif counter == 4:
            poss *= 10*9*8*7
        
        return poss



def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)

if __name__ == "__main__":
    main()