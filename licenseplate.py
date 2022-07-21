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

def perms(total_number, number_of_objects):
    
    prob = 1

    for n in range(number_of_objects):


        print(total_number)
        prob *= total_number
        total_number -= 1

    return prob

class Solution:
    def licensePlate(self,str,len_lett: int = 3, len_num: int =4):
        # type str: string
        # return: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        letters = str[:len_lett]
        numbers = str[len_lett:len_lett+len_num]
        l_counter = 0
        n_counter = 0

        for i in letters:
            if i == ".":
                l_counter += 1

        for n in numbers:
            if n == ".":
                n_counter += 1
        
        return perms(26-len(letters)+l_counter, l_counter) * perms(10-len(numbers)+n_counter, n_counter)



def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)

if __name__ == "__main__":
    main()