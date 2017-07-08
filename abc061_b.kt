
fun main( args : Array<String> ) {
  val (o, n) = readLine()!!.split(" ").map { it.toInt() }

  val m      = mutableMapOf<Int,MutableList<Int>>()
  (1..n).map { 
    val (a, b) = readLine()!!.split(" ").map { it.toInt() }
    if( m[a] == null ) m[a] = mutableListOf<Int>()
    if( m[b] == null ) m[b] = mutableListOf<Int>()
    m[a]!!.add(b)
    m[b]!!.add(a)
  }
  m.toList()
  .sortedBy { kv -> 
    val (k, v) = kv
    k
  }.map { kv ->
    val (k,v) = kv
    println("${v.size}")
  }
}
