#!/usr/bin/env python3
import argparse

def sign(n: int) -> int:
    '''
    Returns -1 if n is negative, 0 if n is 0, else returns 1
    '''
    if n == 0:
        return 0
    return n//abs(n)

def SimpleEuclide(a: int, b:int , verbose:bool = False) -> tuple[int, int, int]:
    '''
    r: reminder of the division a/|b|
    d: dividend such that a - r = d * b
    k, m: coefficients of equation gcd(a,b) = k*n1 + m*n2
    rr: r of the recursive step
    kk, mm: coefficients of the recursive step

    Recursion correctness proof:
    BASE CASES:
    bc1.
        a = d*b         =>  gcd(a,b) = abs(b)
                        =>  (r, k, m) = (abs(b), 0, sign(b))
                        =>  abs(b) = 0*a + sign(b)*b
        Note that the choice of (0, sign(b)) was completely arbitrary.

    bc2.
        a_1 = d_1*b_1 + r_1   
    &&  a_0: b_1, b_0: r_1
    &&  b_1 % r_1 = 0   =>  gcd(a_1,b_1) = r_1
                        =>  (r, k, m) = (r_1, 1, -d_1)
                        =>  r_1 = 1*a_1 -d_1*b_1

    Def
    a_n = d_n * b_n + r_n
    a_(n-1): b_n, b_(n-1): r_n

    a_(n-1) = d_(n-1) * b_(n-1) + r_(n-1)

    By hypothesis at the step n-1 we have
    (r, k, m) = (gcd(a_(n-1), b_(n-1)), C'_(n-1), C''_(n-1))

    gcd(a_(n-1), b_(n-1)) = r_0 = C'_(n-1) * a_(n-1) + C''_(n-1) * b_(n-1)

    But by definition we have
    r_0 = C'_(n-1) * b_n + C''_(n-1) * r_n
        = C'_(n-1) * b_n + C''_(n-1) * (a_n - d_n * b_n)
        = C''_(n-1) * a_n + (C'_(n-1) - d_n * C''_(n-1)) * b_n

    In the code we have:
    rr = kk * a_(n-1) + mm * b_(n-1)

    rr = mm * a_n + (kk - d * mm) * b_n

    => (r, k, m) = (rr, mm, kk - d * mm)

    Moreover we have to prove that the recursion is getting decreasing values
    Again, we can use the previous definition

    call_n takes (a_n, b_n)
    call_(n-1) takes (b_n, r_n)

    Case 1:
    - a_n = b_n is trivial
    
    if a_n = 0 => error, returns (None, None, None)
    if a_n != 0 => r == 0 => bc1

    Case 2:
    - abs(a_n) < abs(b_n)
    => r_n = a_n
    => call_(n-1) takes (b_n, a_n) we are now in Case 3.

    Case 3:
    - abs(a_n) > abs(b_n)

    Since r_n = a_n % abs(b_n)
    abs(r_n) < abs(b_n) < abs(a_n)
    
    call_(n-1)  (b_n, r_n)
    - abs(b_n) < abs(a_n)
    - abs(r_n) < abs(b_n)
    ~>  Both parameters gets closer to 0 at each recursion.
        Since they are integer, this will terminate for sure after a finite amount of steps.
    '''

    if (a*b == 0):
        return (max(abs(a),abs(b)), sign(a), sign(b))

    r = a % abs(b)
    d = (a-r) // b

    if (r == 0): 
        print(f"{a:<4} = {d:>4}*{b:>4} + {r:<4}") if verbose else None
        k = 0
        m = sign(b)
        return (abs(b), k, m)
    elif (b % r == 0):
        print(f"{a:<4} = {d:>4}*{b:>4} + {r:<4}") if verbose else None
        return (r, 1, -d)
    else:
        print(f"{a:<4} = {d:>4}*{b:>4} + {r:<4}") if verbose else None

    rr, kk, mm = SimpleEuclide(b, r, verbose)

    k = mm

    m = kk - d * mm

    return (rr, k, m)


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Euclidean algorithm to find GCD of two numbers')
    
    # Add positional arguments for the two numbers
    parser.add_argument('n1', type=int, help='First number')
    parser.add_argument('n2', type=int, help='Second number')
    
    # Add optional verbose flag
    parser.add_argument('-v', '--verbose', action='store_true', 
                       help='Show step-by-step calculation')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Extract values
    n1 = args.n1
    n2 = args.n2
    verbose = args.verbose
    
    # Here you can call your euclidean algorithm function
    # euclidean_algorithm(a, b, verbose)
    print(f"Numbers: {n1}, {n2}")
    #print(f"Verbose mode: {verbose}")

    print(SimpleEuclide(n1, n2, verbose))

if __name__ == "__main__":
    main()