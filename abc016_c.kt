fun main( args : Array<String> ) {
  val (m, n) = readLine()!!.split(" ").map { it.toInt() }
  val mm     = mutableMapOf<Int, MutableList<Int>>()
  (1..n).map {
    val (a, b) = readLine()!!.split(" ").map { it.toInt() }
    if( mm[a] == null ) mm[a] = mutableListOf<Int>()
    if( mm[b] == null ) mm[b] = mutableListOf<Int>()

    mm[a]!!.add(b)
    mm[b]!!.add(a)
  }
  // search friends of friends...
  val nn = mutableMapOf<Int, MutableSet<Int>>()
  mm.map { kvs ->
    val (k, vs) = kvs
    nn[k] = mutableSetOf<Int>() 
    vs.map { v -> 
       mm[v]!!
        .filter { x -> 
          x != k &&
          !mm[k]!!.contains(x)
        }
        .map { x ->
          nn[k]!!.add( x )
        }
    }
  }
  nn.toList()
  .sortedBy { kv ->
    val (k, v) = kv
    k
  }.map { kv ->
    val (k, v) = kv
    println(v.size)
  }
}
