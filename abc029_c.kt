
fun main(args : Array<String>) {
  val n  = readLine()!!.toInt()
  var bs = mutableSetOf("a", "b", "c")
  (1..n-1).map { 
     val ds = listOf("a", "b", "c").map { x1 ->
       val cs = bs.map { x2 ->
         x2 + x1
       }
       cs
     }.flatMap { x -> x }
     bs = ds.toMutableSet()
  }
  bs.sortedBy { x ->
      x
    }.map { x ->
      println( x )
    }

}
