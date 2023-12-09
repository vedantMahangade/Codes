/*
 * The program is written in Kotlin which was used to develop a Movie App for the Pnumberroject. The program can be executed on below mentioned online kotlin compiler
 * https://play.kotlinlang.org/
 * Copy and Paste the below code into the editor and click on the 'Run' button on the top right corner and the results should appear in the new dialog box below the editore
 * 
 * Counter class with synchronized methods to increment, decrement, and get the value of the counter
 * The @Volatile annotation ensures that changes made by one thread are visible to other threads
 * Please note that the while (true) loop is used to keep the threads running until they successfully update the counter
 * The Thread.yield() is added to allow other threads to run in case the current thread is not able to increment or decrement the counter in a particular iteration.
 */


import kotlin.concurrent.thread


fun main() {
val counter = Counter()


repeat(100) {
thread(name = "Producer-$it") {
while (true) {
if (counter.increment() <= 100) {
println("Producer-$it: Counter = ${counter.get()}")
break
}
Thread.yield()
}
}
}


repeat(100) {
thread(name = "Consumer-$it") {
while (true) {
if (counter.decrement() >= 0) {
println("Consumer-$it: Counter = ${counter.get()}")
break
}
Thread.yield()
}
}
}
}


class Q3 {
@Volatile
private var counter = 0


fun increment(): Int {
synchronized(this) {
return if (counter < 100) ++counter else counter
}
}


fun decrement(): Int {
synchronized(this) {
return if (counter > 0) --counter else counter
}
}


fun get(): Int {
return counter
}
}