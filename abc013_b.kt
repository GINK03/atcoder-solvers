import java.lang.Math
fun main( args : Array<String>) {
   val (a,b) = (1..2).map{ readLine()!!.toInt() }
   val c = b + 10
   val d = b - 10
   listOf(Math.abs(a - d), Math.abs(c - a), Math.abs(b - a)).min().let { println(it) }
}
