
fun main(args : Array<String> ) { 
  val m:MutableMap<Char, Int> = mutableMapOf()
  readLine()!!.toList().map { x ->
    if( m.get(x) == null ) 
      m[x] = 0
    m[x] = m[x]!! + 1
  }
  val r = m.all { xy ->
    val (x, y) = xy
    y%2 == 0
  }
  when(r) {
    true -> println("Yes")
    false -> println("No")
  }
}
