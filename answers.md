  # CMPS 6610 Problem Set 01
## Answers

**Name:** Chanuka Ravishan Algama (calgama@tulane.edu)


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not?

      Finding c and n_o such that for all c > 0 and n > n_o,  2^(n+1) <= c . 2^n

      let c = 2, and n_o = 1

      Then for all n > n_o

      $2^{n+1} \in O(2^n)$

      Therefore the statement is TRUE

  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?

      let x = 2^n

      then, 2^x >= x for all n >= 0

      Theirfore, the statement is FALSE
 
  - 1c. Is $n^{1.01} \in O(\mathrm{\log}^2 n)$?

      Finding c and n_o such n^1.01 <= c log^2n

      g(n) / f(n) = n^1.01 / log^2n

                  = $\lim_{x \to \infty} n^1.01 / log^2n

                  = \infty

      This means that g(n) grows faster than f(n), and the ratio doesn't stay bounded by any constant c

      Theirfore, the statement is FALSE

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{\log}^2 n)$?

      As proven above n^1.01 grows faster than log^2n, and the ratio doesn't stay bounded by any constant c

      Theirfore, the statement is TRUE

  - 1e. Is $\sqrt{n} \in O(\mathrm{\log}^3 n)$?

      Finding c and n_o such n^0.5 <= c log^3n

      g(n) / f(n) = n^0.5 / log^3n

                  = $\lim_{x \to \infty} n^0.5 / log^3n

                  = \infty

      This means that g(n) grows faster than f(n), and the ratio doesn't stay bounded by any constant c

      Theirfore, the statement is FALSE

  - 1f. Is $\sqrt{n} \in \Omega(\mathrm{\log}^3 n)$?

      As proven above n^0.5 grows faster than log^3n, and the ratio doesn't stay bounded by any constant c

      Theirfore, the statement is TRUE

  - 1g. Prooving that $o(g(n)) \cap \omega(g(n))$ is the empty set.

      Lets assume there is a set that $o(g(n)) \cap \omega(g(n))$

      f(n) \in \Omega(g(n)) states that,

            = f(n) <= c g(n) , for c> 0 and n > 0

      f(n) \in w(g(n)) states that,

            = f(n) >= c g(n) , for c> 0 and n > 0

      Therefore c g(n) < f(n) < c g(n)






2. **SPARC to Python**

  - 2b

3. **Parallelism and recursion**

  - 3b

  - 3d

  - 3e
  
4. **GCD**
