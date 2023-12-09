# Design-Analysis-of-Algorithm---CSCI-6212---Project-Code
A repository to host project code for the course Design &amp; Analysis of Algorithm (CSCI 6212)

## DAA Project Code 1.py: 
  Python program written for below Psuedo Code.
  ```psuedo
  for (int i = 1 to n) {
    j=i
    while (j < n) {
      k=j
      while (k < n) {
        Sum += a[i]*b[j]*c[k]
        k += log log n
      }
      j += log (j+10)
    }
  }
  ```
## DAA Project Code 2.py: 
  Python program written to calculate Convex Hull of Set P of n points using a O(nLog(n)) Divide and Conquer Algorithm.

## Q1.kt:
  A higher-order function, or functional form, is one that either takes one or more functions as parameters or yields a function as its result, or both. One common kind of functional form is function composition, which has two functional parameters and yields a function whose value is the first actual parameter function applied to the result of the second. Function composition is written as an expression, using as ° an operator, as in

  h ≡ f  ° g

  For example, if

  f(x) ≡ x + 2

  g(x) ≡ 3 * x

  then h is defined as

  h(x) ≡ f(g(x)), or h(x) ≡ (3 * x) + 2

  Using the Kotlin programming language you have been developing your project, develop a small program that implements a high-order function ACCORDING to this specification. (See Sebesta's book, section 15.2.2)

## Q2.kt:

Section 11.4.2.4 An Example" from Sebesta's book provides an exemple of an ADT (Abstract Data Type) implemented in C++. Provide an implementation of the same ADT using the Kotlin programming language you used in your project. If your selected programming language does not provide full support to OO, but it allows you to define Structs and methods attached to Structs, please use this approach.

## Q3.kt:


This question is related to concurrency as discused in the Chapter 13 of the Sebesta's book. 

Assuming you have a mutable variable, counter, initialized as zero, using the programming language you developed your project (or if you prefer you can use Scala, Rust, Julia, or Go) run 100 concurrent threads, named producer, where each concurrent thread adds 1 to counter, and 100 concurrent threads, named consumer, where each concurrent threads substract 1 from counter. Everytime counter changes its value, prints the new value. 

Contraints:

The value of counter should never be lower than zero or greater than 100.
At the end of the execution of these 200 concurrent threads, counter should be equal to zero.
Each concurrent threds ends after adding1 to or subtraction 1 from counter
Concurrent threats should not have priorities
Producer and Consumer concurrent threads should be initialized at the same time. You shall not initialize consumer threats after producer threads: both type of threads shall be run concurrently and initalized at the same time. In other words, you program should not ditacte the order the currently treats will be executed.

## Q4.clj:x

Using Clojure progamming language, develop a script that list the 10 most common words in the following book ignoring the stops English words (https://www.ranks.nl/stopwords)

Moby Dick; Or, The Whale by Herman Melville
A text version of this book is available in the following URL:
https://www.gutenberg.org/cache/epub/2489/pg2489.txt
