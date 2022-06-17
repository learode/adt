class Polynomial:
    def __init__(self, *coefficients):
        """Input a tuple of coefficients in the form a_n, ... a_1, a_0"""

        self.coefficients = list(coefficients) # tuple to list
        self.size = len(coefficients)
        self.degree = self.size - 1 # Using the index as the power/degree
         
    def __repr__(self):
        """Return a string representation of a polynomial"""
        return str(tuple(self.coefficients))

    def expression(self):
        def x_expresion(deg):
            """Append x with its degree to the coefficient"""
            if deg == 0:
                re = ""
            elif deg == 1:
                re = "x"
            else:
                re = "x^"+str(deg)
            return re
             
        expression_str = "" 
        
        for i in range(0, self.degree +1):
            cof = self.coefficients[i]
            
            if cof != 0:
                # append + or - before each term
                expression_str += f"{' + ' if cof>0 else ' - '}{abs(cof)}{x_expresion(self.degree-i)}"
                
        return expression_str.strip(" + ") # removing leading +
    # End of expression.

    def evaluate(self, x):
        """Using Horner's scheme to evaluate the polynomial"""
        sum = self.coefficients[0]
        
        for i in range(1, self.size):
            sum = sum*x + self.coefficients[i]
        return sum;
    # End of evaluate,

    def scalar_multiple_by(self, k):
        """Multiple the polynomial with a constant"""
        
        k_expression = [] # temporary hold for the list of coefficients

        for i in range(0, self.size):
            k_expression.append(self.coefficients[i] * k)

        self.coefficients = k_expression # re-assigning value of coeficient to the new coef
        
        return k_expression
    # End of scalar_multiple_by,

    def add(self, other):
        """Add poly1 to this polynomial
            that_poly should by a string of coefficeints separated by , or 
            an instances of this class
        """
        dif = abs(self.size - other.size)
        sum = [];
        here = []
        there = []
        
        if self.size <= other.size:
            here = [0]*dif + self.coefficients
            there = other.coefficients
            longest = other.size
        if self.size > other.size:
            here = self.coefficients
            there = [0]*dif + other.coefficients
            longest = self.size
            
        for i in range(0, longest):
            sum.append(there[i] + here[i])
        return sum;
    # End of add
        
            
# End of Class Polynomial

qua = Polynomial(3 ,2)

#print(qua.expression())
#print(qua.evaluate(2))

q = Polynomial(1, 3, 9)
#print(q.expression())
print(qua, q)

print(q.add(qua))
#print(q.evaluate(1))
#print(q.scalar_multiple_by(4))

#print(q.expression())