fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  val a1 = readLine()!!.split(" ").map(String::toInt)
  val a2 = readLine()!!.split(" ").map(String::toInt)
  val a3 = readLine()!!.split(" ").map(String::toInt)
 
  val c2 = a2.toSet().map { b2 ->
    a3.filter { b3 -> 
      if( b2 < b3 ) true
      else false 
    }.size.let { Pair(b2, it) }
  }.toMap()
  
  val c1 = a1.map { b1 ->
    a2.filter { b2 ->
      if( b1 < b2 ) true
      else false 
    }.map { 
      c2[it]!!
    }.sum()
  }.sum()
  println(c1)
}
