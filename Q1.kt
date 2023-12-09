/*

The program is written in Kotlin which was used to develop a Movie App for the Project. The program can be executed on below mentioned online kotlin compiler
https://play.kotlinlang.org/
Copy and Paste the below code into the editor and click on the 'Run' button on the top right corner and the results should appear in the new dialog box below the editor.package

The value passed to the funciton h() can be replaced to test for different values of x, such as h(10), h(-12)

Function composition in Kotlin can be implemented using a operator function in this case it is 'compose'. The 'compose' function is defined as an infix function that takes a function f and another function g and returns a new function representing the composition of f and g that is f(g(x))

*/

fun main() {
    val f: (Int) -> Int = { x -> x + 2 }
    val g: (Int) -> Int = { x -> 3 * x }
    
    //Function Composition
    val h: (Int) -> Int = compose(f, g)
    
    val result = h(5)
    println("h(5) = $result")
    }
    
    // Function composition
    fun <P1, P2, R> compose(f: (P1) -> P2, g: (P2) -> R): (P1) -> R = { x -> g(f(x)) }