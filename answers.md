  # CMPS 6610 Problem Set 01
## Answers

**Name:** Chanuka Ravishan Algama (calgama@tulane.edu)


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not?

      Finding c and $n_o$ such that for all $c > 0$ and $n > n_o$,   $2^{n+1} <= c . 2^n$

      let $c = 2, and n_o = 1$

      Then for all $n > n_o$

      $2^{n+1} \in O(2^n)$

      Therefore the statement is TRUE

  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?

      let $x = 2^n$

      then, $2^x >= x$ for all $n >= 0$

      Therefore, the statement is FALSE
 
  - 1c. Is $n^{1.01} \in O(\mathrm{\log}^2 n)$?

      Finding c and $n_o$ such $n^{1.01} <= c log^2n$

      $ \frac{g(n)}{f(n)} = \frac{n^{1.01}}{log^2n}$

                 $ = \lim_{x \to \infty} n^1.01 / log^2n$

                 $ = \infty $

      This means that g(n) grows faster than f(n), and the ratio doesn't stay bounded by any constant c

      Theirfore, the statement is FALSE

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{\log}^2 n)$?

      As proven above $n^{1.01}$ grows faster than $log^2n$, and the ratio doesn't stay bounded by any constant c

      Theirfore, the statement is TRUE

  - 1e. Is $\sqrt{n} \in O(\mathrm{\log}^3 n)$?

      Finding c and n_o such $n^{0.5} <= c log^3n$

      $$g(n) / f(n) = n^0.5 / log^3n

                  = \lim_{x \to \infty} n^{0.5} / log^3n

                  = \infty$$

      This means that g(n) grows faster than f(n), and the ratio doesn't stay bounded by any constant c

      Theirfore, the statement is FALSE

  - 1f. Is $\sqrt{n} \in \Omega(\mathrm{\log}^3 n)$?

      As proven above $n^{0.5}$ grows faster than $log^3n$, and the ratio doesn't stay bounded by any constant c

      Theirfore, the statement is TRUE

  - 1g. Prooving that $o(g(n)) \cap \omega(g(n))$ is the empty set.

      Lets assume there is a set that $o(g(n)) \cap \omega(g(n))$

      $f(n) \in \Omega(g(n))$ states that, 

            There exists a c > 0 and $n_0$ such that for all $n > n_0 f(n) <= c g(n)$

      $f(n) \in w(g(n))$ states that,

            For all c > 0, there exists n_0 such that for all $n > n_0  f(n) >= c g(n)$

      Therefore $c g(n) < f(n) < c g(n)$ cannot hold. There cannot hold any f(n) that satisfy this inequality.




2. **SPARC to Python**

  - 2b The function takes in two arguments, the definition looks like an attempt to implement a function to return the greatest common divider but its not. The function returns the largest value out of the two inputs.

  - 2c

      A constant work O(1) is done in every recursive call. There are two comparisons at the beginning, followed by a minimum, a maximum, a modulus, and a recursive function call. In the recursive call, the second argument gets smaller and quickly becomes 0.

      Work = No of steps * Work done in each step

	        W= O(log(min(a,b))) * O(1)

	        W = O(log(min(a,b)))

      Span = Critical path length

	        S = O(min(a,b))

3. **Parallelism and recursion**

  - 3b W(n) = O(n)  (we iterate the for loop with n elements, and inside a loop a constant work is being done, so the work is linearly proportional to the input)

      S(n) = O(n)   (critical path length)

  - 3d

      W(n) = 2W(n/2) + 1

      S(n) = S(n/2) + 1

  - 3e

      Work and Span will be the same as in 3d, due to each recursive call involving similar amount of work done in constant times


