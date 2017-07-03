
fun main( args : Array<String> ) {
  val a1 = readLine()!!.toList().map { it.toString() }
  val a2 = readLine()!!.toList().map { it.toString() }
  val store = "atcoder".toList().map { it.toString() }.toMutableList()

  val discted = a1.zip(a2).map { kv ->
    val (k,v) = kv
    Pair(k,v)
  }.filter { kv ->
    val (k,v) = kv
    k != v
  }
  val allat = discted.map { kv ->
    val (k,v) = kv
    when {
      k == v -> "Exist"
      else -> null
    }
  }.filter { 
    it != null
  }
  
  var noExist = false
  discted.filter { kv ->
    val (k,v) = kv
    k != v
  }.map { kv -> 
    val (k, v) = kv
    when { 
      k == "@" -> v
      v == "@" -> k
      else -> noExist == true
    }
  }.map { x ->
    if( !store.contains(x) ) noExist = true
    store.remove( x )
  }
  when { 
    noExist -> "You will lose"
    store.size >= allat.size -> "You can win"
    else -> "You will lose"
  }.let { println(it) }
}
