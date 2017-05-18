
fun main(args : Array<String>) { 
  val (n, m) = readLine()!!.split(" ").map { x-> x.toInt() }
  val ba     = (1..n).map { 0 }.toMutableList()
  (1..m).map {
   val (a, b, c) = readLine()!!.split(" ").map { x-> x.toInt() }
   (a-1 .. b-1).map { x-> 
     ba[x] = c
   }
  }
  ba.map { x->
    println(x)
  }
}
