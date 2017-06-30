
fun main( args : Array<String> ) { 
  val n  = readLine()!!.toInt()
  val ms = readLine()!!.split(" ").map { it.toInt() }.sorted().reversed()
  val m  = mutableMapOf<Int, MutableList<Int>>()

  ms.mapIndexed { i,x -> 
    val ff = i/2
    if( m[ff] == null) m[ff] = mutableListOf()
    m[ff]?.let { it.add(x) }
  }

  m.map { kv -> 
    val (k, v) = kv
    when { 
      v.size != 1 -> v.min()!!.toInt()
      else        -> 0
    }
  }.reduce { y,x ->
    y+x
  }.let { println(it) }
}
