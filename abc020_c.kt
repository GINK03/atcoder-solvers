
fun main(args:Array<String>) {
  val (H,W,T) = readLine()!!.split(" ").map(String::toInt)

  val ys = (1..H).map { readLine()!! }
  // build patterns

  var xs = mutableListOf<MutableList<Triple<Int,Int,Char>>>( mutableListOf(Triple(0,0,'S')) )
  
  var gs = mutableListOf<MutableList<Triple<Int,Int,Char>>>( )
  for(d in (0..1000)) {
    val ress = mutableListOf<MutableList<Triple<Int,Int,Char>>>( )
    for( x in xs ) {
      var next = mutableListOf<Triple<Int,Int,Char>>()
      val p = x.last()
      if( ys[p.second][p.first] == 'G' ) { gs.add(x); continue }
      // under
      try {
        val char = ys[p.second+1][p.first] 
        if( !x.contains(Triple(p.first, p.second+1, char)) ) next.add( Triple(p.first, p.second+1, char) )
      } catch ( e : Exception ) { }
      // right
      try {
        val char = ys[p.second][p.first+1] 
        if( !x.contains(Triple(p.first+1, p.second, char)) ) next.add( Triple(p.first+1, p.second, char) )
      } catch ( e : Exception ) { }
      // left
      try {
        val char = ys[p.second][p.first-1] 
        if( !x.contains(Triple(p.first-1, p.second, char)) ) next.add( Triple(p.first-1, p.second, char) )
      } catch ( e : Exception ) { }
      // up
      try {
        val char = ys[p.second-1][p.first] 
        if( !x.contains(Triple(p.first, p.second-1, char)) ) next.add( Triple(p.first, p.second-1, char) )
      } catch ( e : Exception ) { }
      // build up
      next.map { n -> 
        val a = x.toMutableList()  
        a.add(n)
        ress.add(a)
      }
    }
    if( ress.size == 0 ) break
    xs = ress  
  }

  // gsからコストを算出
  gs.map { g ->
    val dots = g.filter { it.third == '.' }.size
    val sharps = g.filter { it.third == '#' }.size
    ( T-1-dots )/sharps
  }.max()!!.run(::println)
}
