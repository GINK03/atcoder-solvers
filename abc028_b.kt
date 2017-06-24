
fun main( args : Array<String> ) { 
  val m = mutableMapOf<Char, Int>()
  "ABCDEF"
   .toList()
   .map { x ->
     m[x] = 0
   }

  readLine()!!
    .toList()
    .map { x ->
      m[x] = m[x]!! + 1
    }
  
  val ans = m.toList()
    .sortedBy { x ->
      x.first 
    }.map { xy ->
      xy.second
    }.joinToString(" ")
  println( ans )
}

