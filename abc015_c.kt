
fun main( args : Array<String> ) {
  val (m, n) = readLine()!!
                .split(" ")
                .map { it.toInt() }
  var chaine = mutableSetOf<MutableList<Int>>( mutableListOf<Int>( ) )
  (1..m).map { 
    readLine()!!
      .split(" ")
      .map { it.toInt() }
      .toSet()
      .toList()
  }.map { xs ->
    val nextChaine = mutableSetOf<MutableList<Int>>()
    chaine.map { c ->
      xs.map { x ->
        val c2 = c.toMutableList()
        c2.add(x)
        c2
      }.map { c ->
        nextChaine.add(c)
      }
    }
    chaine = nextChaine
  }
  chaine.map { xs ->
    xs.reduce { y,x -> 
      y xor x
    }
  }.let {
    when (it.contains(0)) {
      true -> "Found"
      else -> "Nothing"
    }.let { println(it) }
  }
}
