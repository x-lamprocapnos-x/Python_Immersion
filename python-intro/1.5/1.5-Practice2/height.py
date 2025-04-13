class height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def total_inches(self):
        # Method to convert height to total inches
        return self.feet * 12 + self.inches

    def __lt__(self, other):
        # Less than method, overload the < operator
        return self.total_inches() < other.total_inches()

    def __le__(self, other):
        # Less that or equal to method, overload the <= operator
        return self.total_inches() <= other.total_inches()

    def __eg__(self, other):
        # Equal to method, overload the == operator
        return self.total_inches() == other.total_inches()

    def __gt__(self, other):
        # Greater than method, overload the > operator
        return self.total_inches() > other.total_inches()

    def __ge__(self, other):
        # Greater than or equal to method, overload the >= operator
        return self.total_inches() >= other.total_inches()

    def __ne__(self, other):
        # Not equal to method, overload the != operator
        return self.total_inches() != other.total_inches()
    
    # Define the subtract method
    # def __sub__(self, other):
    #     # Overload the operator to subtract two heights
    #     total_inches_self = self.feet * 12 + self.inches
    #     total_inches_other = other.feet * 12 + other.inches

    #     # Perform the subtraction
    #     result_inches = total_inches_self - total_inches_other

    #     # Handle the negative results 
    #     if result_inches < 0:
    #         raise ValueError("Height cannot be negative")

    #     # Convert the results back to feet and inches
    #     result_feet = result_inches // 12
    #     result_remaining_inches = result_inches % 12

    #     # return new height object
    #     return height(result_feet, result_remaining_inches)

    def __str__(self):
        # Return a string with the height details
        return f"{self.feet} feet and {self.inches} inches"

# Create two height objects
height1 = height(4, 6) # 4 feet 6 inches
height2 = height(4, 5) # 4 feet 5 inches
height3 = height(5, 9) # 3 feet 9 inches
height4 = height(5, 10) # 5 feet 10 inches

# Test cases
print("Height(4, 6) > Height(4, 5):", height1 > height2)
print("Height(4, 5) >= Height(4, 5):", height2 >= height2)
print("Height(5, 9) != Height(5, 10):", height3 != height4)

# Subtract the two heights
# try:
#     result = height1 - height2
#     print("Resulting height: ", result) 
# except ValueError as e:
#     print(e)