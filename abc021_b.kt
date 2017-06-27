
fun main( args : Array<String> ) { 
   val a  = readLine()?.let { it.toInt() }
   val (first, last) = readLine()!!.let { it.split(" ").map { it.toInt() } }
   val b  = readLine()?.let { it.toInt() }
   val cs = readLine()?.let { it.split(" ").map { it.toInt() } }!!.toMutableSet()
   cs.add(first)
   cs.add(last)
   when { 
     cs.size == b!! + 2 -> println("YES")
     else         -> println("NO")
   }
}
