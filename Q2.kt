/*

 * The program is written in Kotlin which was used to develop a Movie App for the Pnumberroject. The program can be executed on below mentioned online kotlin compiler
 * https://play.kotlinlang.org/
 * Copy and Paste the below code into the editor and click on the 'Run' button on the top right corner and the results should appear in the new dialog box below the editore
 * 
 * The Code defines a Stack class with methods for pushing, popping, checking the top element, and checking if the stack is empty. 
 * The main function creates a stack object, performs some operations, and prints the top elements.
 * 
 * The class encapsulates the behavior of a stack, and its internal details are hidden from the user. 
 * The Stack class abstracts away the complexities of managing the underlying array and topSub index.
 * The internal representation of the stack is hidden from the outside world.
 * The methods push, pop, top, empty provide a controlled interface to manipulate the stack ensuring integrity of the data structure. 
 * 
 * The class itself serves as an abstract data type by following principles of abstraction, encapsulation, information hiding, and data integrity collectively contribute to the implementation of an abstract data type in this code.
 */


class Stack {
    private val stackArray = IntArray(100)
    private var topSub = -1
    
    
    fun push(number: Int) {
    if (topSub == stackArray.size - 1) {
    println("Error in push - stack is full")
    } else {
    stackArray[++topSub] = number
    }
    }
    
    
    fun pop() {
    if (topSub == -1) {
    println("Error in pop - stack is empty")
    } else {
    topSub--
    }
    }
    
    
    fun top(): Int {
    return if (topSub >= 0) {
    stackArray[topSub]
    } else {
    println("Error in top - stack is empty")
    -1 // Return a default value or throw an exception as needed
    }
    }
    
    
    fun empty(): Boolean {
    return topSub == -1
    }
    }
    
    
    fun main() {
    val myStack = Stack()
    
    
    myStack.push(5)
    myStack.push(3)
    
    
    val temp1 = myStack.top()
    println("Top element is: $temp1")
    
    
    myStack.pop()
    
    
    val temp2 = myStack.top()
    println("Top element is: $temp2")
    
    
    val temp3 = myStack.top()
    println("Top element is: $temp3")
    
    
    myStack.pop()
    }