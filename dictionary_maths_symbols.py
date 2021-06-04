print("Welcome to mathematics dictionary")
print("  \n\nEnter 1 for +")
print(" Enter 2 for -")
print(" Enter 3 for *")  # Giving menu
print(" Enter 4 for /")
print(" Enter 5 for a^b")
print(" Enter 6 for ppm")
print(" Enter 7 for ppb")
print(" Enter 8 for ε")
print(" Enter 9 for e")
print(" Enter 10 for y'")
print(" Enter 11 for P(A)")
print(" Enter 12 for U ")
print(" Enter 13 for º")
print(" Enter 14 for μ")
print(" Enter 15 for ∫")
print(" Enter 16 for >")
print(" Enter 17 for <")
print(" Enter 18 for ≤")
print(" Enter 19 for ≥")
print(" Enter 20 for ||")
print(" Enter 21 for π")
print(" Enter 22 for ∑")
print(" Enter 23 for ∆")
print(" Enter 24 for ∞")
print(" Enter 25 for ~ ")
print(" Enter 26 for %")
print(" Enter 27 for f(x)")
print(" Enter 28 for F(x)")
print(" Enter 29 for y' ")
print(" Enter 30 for (a,b)")

choice = int(input("\n\n Enter your choice="))  # taking choice input

if choice == 1:
    print("Addition sign\nSum of a few values\n3 + 5 = 8")  # Checking and giving required output

elif choice == 2:
    print("Subtraction is an arithmetic operation that represents the operation of removing objects from a collection. "
          "The result of a subtraction is called a difference. Subtraction is signified by the minus sign (−).")

elif choice == 3:
    print("A mathematical operation performed on a pair of numbers in order to derive a third number called a product. "
          "For positive integers, multiplication consists of adding a number (the multiplicand) to itself a specified "
          "number of times. Thus multiplying 6 by 3 means adding 6 to itself three times.")

elif choice == 4:
    print("In mathematics, the word division means the operation which is the opposite of multiplication. Some symbols "
          "for division can be a slash, a line, or the division sign. Each, of those three, means 6 divided by 3 with "
          "2 as the answer")

elif choice == 5:
    print("The exponent of a number says how many times to use the number in a multiplication. In 82 the 2 says to use "
          "8 twice in a multiplication, so 82 = 8 × 8 = 64. In words: 82 could be called 8 to the power 2 or 8 to the "
          "second power, or simply 8 squared Exponents are also called Powers or Indices.")

elif choice == 6:
    print("ppm per-million    1ppm = 1/1000000   10ppm × 30 = 0.0003")

elif choice == 7:
    print("ppb per-billion    1ppb = 1/1000000000    10ppb × 30 = 3×10-7")

elif choice == 8:
    print("epsilon represents a very small number, near zero  ε → 0")

elif choice == 9:
    print("e constant / Euler's number e = 2.718281828... e = lim (1+1/x)x , x→∞")

elif choice == 10:
    print("In mathematics, the derivative is a way to show rate of change: that is, the amount by which a function is "
          "changing at one given point.For functions that act on the real numbers, it is the slope of the tangent line "
          "at a point on a graph.")

elif choice == 11:
    print("Symbol name- probability function")

elif choice == 12:
    print("Union symbol    ")

elif choice == 13:
    print("Degree symbol\nAngular measure Temperature")

elif choice == 14:
    print("Greek mu \nmicro- (10-6)")

elif choice == 15:
    print("Integration is a way of adding slices to find the whole. Integration can be used to find areas, volumes, "
          "central points and many useful things. But it is easiest to start with finding the area under the curve ")

elif choice == 16:
    print("Strictly inequality sign which shows that one number is greater than other")

elif choice == 17:
    print("Strictly inequality sign which shows that one number is less than other")

elif choice == 18:
    print("Inequality sign which shows that one number is greater than equal to other")

elif choice == 19:
    print("Inequality sign which shows that one number is less than equal to other")

elif choice == 20:
    print("Symbol indicates relationship between two lines which are parallel")

elif choice == 21:
    print("Symbol name:pi constant \nπ=3.14159... is the ratio between the circumference and diameter of a circle")

elif choice == 22:
    print("Symbol name: Sigma \nSummation- sum of all values in range of series")

elif choice == 23:
    print("Symbol name: Delta \nShows change/difference between any two quantities")

elif choice == 24:
    print("Symbol name: Infinity \nIt represents an infinitely large number")

elif choice == 25:
    print("Symbol name: approximately equal \nIt is commonly used as shorthand for 'is approximately equal to'...")

elif choice == 26:
    print("Symbol name: Percentage \nIt represents proportion   1%=1/100=0.1%")

elif choice == 27:
    print("Symbol name: probability density function(pdf) of x \nmaps values of x to f(x) \nP(a≤x≤b)=∫f(x)dx")

elif choice == 28:
    print("Symbol name: cumulative distribution function(cdf) of x \nF(x)=P(X≤x)")

elif choice == 29:
    print("Symbol name: derivative \nderivative-Leibniz's notation")

elif choice == 30:
    print("Symbol name: close interval \n[a,b]={a≤x≤b}")

else:
    print("Invalid Entry")
