#User Guide 
#https://docs.python.org/3/library/math.html
#Real number
def RealNumberInstructions(): 
    print("\nReal Number Instructions\n")

    print("ceil(x)")
    print("The ceiling of x, the smallest integer greater than or equal to x.")
    print("comb(n, k)")
    print("The number of ways to choose k items from n items without repetition and without order.")
    print("copysign(x, y)")
    print("A float with the magnitude (absolute value) of x but the sign of y. On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.")
    print("fabs(x)")
    print("The absolute value of x.")
    print("factorial(x)")
    print("x factorial as an integer.")
    print("floor(x)")
    print("The floor of x, the largest integer less than or equal to x. If x is not a float, delegates to x.__floor__(), which should return an Integral value.")
    print("fmod()")
    print("Generally preferred when working with floats, while x % y is preferred when working with integers.")
    print("frexp(x)")
    print("The mantissa and exponent of x as the pair (m, e). m is a float and e is an integer such that x == m * 2**e exactly. If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m) < 1. This is used to “pick apart” the internal representation of a float in a portable way.")
    print("fsum(iterable)")
    print("An accurate floating point sum of values in the iterable. Avoids loss of precision by tracking multiple intermediate partial sums:")
    print("sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])")
    print("0.9999999999999999")
    print("sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])")
    print("1.0")
    print("gcd(*integers)")
    print("The greatest common divisor of the specified integer arguments. If any of the arguments is nonzero, then the returned value is the largest positive integer that is a divisor of all arguments. If all arguments are zero, then the returned value is 0. gcd() without arguments returns 0.")
    print("isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)")
    print("True if the values a and b are close to each other and False otherwise.")
    print("isfinite(x)")
    print("True if x is neither an infinity nor a NaN, and False otherwise. (Note that 0.0 is considered finite.)")
    print("isinf(x)")
    print("True if x is a positive or negative infinity, and False otherwise.")
    print("isnan(x)")
    print("True if x is a NaN (not a number), and False otherwise.")
    print("isqrt(n)")
    print("The integer square root of the nonnegative integer n. This is the floor of the exact square root of n, or equivalently the greatest integer a such that a² ≤ n.")
    print("lcm(*integers)")
    print("The least common multiple of the specified integer arguments. If all arguments are nonzero, then the returned value is the smallest positive integer that is a multiple of all arguments. If any of the arguments is zero, then the returned value is 0. lcm() without arguments returns 1.")
    print("ldexp(x, i)")
    print("x * (2**i). This is essentially the inverse of function frexp().")
    print("modf(x)")
    print("The fractional and integer parts of x. Both results carry the sign of x and are floats.")
    print("math.nextafter(x, y)")
    print("The next floating-point value after x towards y.")
    print("perm(n, k=None)")
    print("The number of ways to choose k items from n items without repetition and with order.")
    print("prod(iterable, *, start=1)")
    print("Calculate the product of all the elements in the input iterable. The default start value for the product is 1.")
    print("remainder(x, y)")
    print("The IEEE 754-style remainder of x with respect to y. For finite x and finite nonzero y, this is the difference x - n*y, where n is the closest integer to the exact value of the quotient x / y. If x / y is exactly halfway between two consecutive integers, the nearest even integer is used for n. The remainder r = remainder(x, y) thus always satisfies abs(r) <= 0.5 * abs(y).")
    print("trunc(x)")
    print("The Real value x truncated to an Integral (usually an integer). Delegates to ")
    print("ulp(x)")
    print("The value of the least significant bit of the float x:")
    print("exp(x)")
    print("e raised to the power x, where e = 2.718281… is the base of natural logarithms. This is usually more accurate than math.e ** x or pow(math.e, x).")
    print("expm1(x)")
    print("e raised to the power x, minus 1. Here e is the base of natural logarithms. For small floats x, the subtraction in exp(x) - 1 can result in a ")
    print("exp(1e-5) - 1")
    print("1.0000050000069649e-05")
    print("expm1(1e-5)")
    print("1.0000050000166668e-05")
    print("math.log(x[, base])")
    print("With one argument, return the natural logarithm of x (to base e).")
    print("With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).")
    print("log1p(x)")
    print("The natural logarithm of 1+x (base e). The result is calculated in a way which is accurate for x near zero.")
    print("math.log2(x)")
    print("The base-2 logarithm of x. This is usually more accurate than log(x, 2).")
    print("log10(x)")
    print("The base-10 logarithm of x. This is usually more accurate than log(x, 10).")
    print("pow(x, y)")
    print("x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. ")
    print("sqrt(x)")
    print("The square root of x.")
    print("acos(x")
    print("The arc cosine of x, in radians. The result is between 0 and pi.")
    print("math.asin(x)")
    print("The arc sine of x, in radians. The result is between -pi/2 and pi/2.")
    print("atan(x)")
    print("The arc tangent of x, in radians. The result is between -pi/2 and pi/2.")
    print("atan2(y, x)")
    print("atan(y / x), in radians. The result is between -pi and pi.")
    print(".cos(x)")
    print("The cosine of x radians.")
    print("math.sin(x)")
    print("The sine of x radians.")
    print("math.tan(x)")
    print("The tangent of x radians.")
    print("degrees(x)")
    print("Convert angle x from radians to degrees.")
    print("radians(x)")
    print("Convert angle x from degrees to radians.")
    print("acosh(x)")
    print("The inverse hyperbolic cosine of x.")
    print("asinh(x)")
    print("The inverse hyperbolic sine of x.")
    print("math.atanh(x)")
    print("The inverse hyperbolic tangent of x.")
    print("cosh(x)")
    print("The hyperbolic cosine of x.")
    print("sinh(x)")
    print("The hyperbolic sine of x.")
    print("tanh(x)")
    print("The hyperbolic tangent of x.")
    print("math.erf(x)")
    print("The error function at x.")
    print("math.erfc(x)")
    print("The complementary error function at x.") 
    print("gamma(x)")
    print("The Gamma function at x.")
    print("lgamma(x)")
    print("The natural logarithm of the absolute value of the Gamma function at x.")
    print("pi")
    print("The mathematical constant π = 3.141592…, to available precision.")
    print("e")
    print("The mathematical constant e = 2.718281…, to available precision.")
    print("tau")
    print("The mathematical constant τ = 6.283185…, to available precision. Tau is a circle constant equal to 2π, the ratio of a circle’s circumference to its radius.")
    print("inf")
    print("A floating-point positive infinity. (For negative infinity, use -math.inf.) Equivalent to the output of float('inf').")
    print("nan")
    print("A floating-point “not a number” (NaN) value. Equivalent to the output of float('nan').")
    print("")

#Complex number 
def ComplexNumberInstructions(): 
    print("\Complex Number Instructions\n")
#Derivatives 
def DerivativesInstructions(): 
    print("\nDerivatives Instructions\n")
    print("It has different eight derivatives rules: Simple, Power, Product, Quotient, Chain, Exponential, Partial and Multivariable. For example, you can type 'deriv(x**2, x)''.")  
    
#integral 
def IntegralInstructions(): 
    print("\nIntegral Instructions\n")    
    print("It has infinite and definite integrals. For example, you can type 'integral(2*x,x)' or 'integral(2*x, x, 1, 2)'")
#Statistics 
def StatisticsInstructions(): 
    print("\nStatistics Instructions\n")

    print("mean()                Arithmetic mean (average) of data.")
print("fmean()               Fast, floating point arithmetic mean.")
print("geometric_mean()      Geometric mean of data.")
print("harmonic_mean()       Harmonic mean of data.")
print("median()              Median (middle value) of data.")
print("median_low()          Low median of data.")
print("median_high()         High median of data.")
print("median_grouped()      Median, or 50th percentile, of grouped data.")
print("mode()                Mode (most common value) of data.")
print("multimode()           List of modes (most common values of data).")
print("quantiles()           Divide data into intervals with equal probability.")

#Algebra 
def AlgebraInstructions(): 
    print("\nAlgebra Instructions\n")
    print("Usuing simplify() - Simplifies the given expression.")
    print("poly() - Efficiently transform an expression into a polynomial.")
    print("factor() - The factor of given expression.")
    print("Expand() - Expands the given expression")
#Matrix 
def MatrixInstructions(): 
    print("\nMatrix Instructions\n")