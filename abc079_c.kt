
fun main(args:Array<String>) {
  val bs = readLine()!!.toList().map(Char::toString).map(String::toInt)

  val fl = listOf( {it:Int -> 1*it }, { it:Int -> -1*it } )

  val af = { (0..1) } 

  val results = mutableListOf<Pair<Int, List<String>>>()
  (0..0).map { a1 -> af().map { a2 -> af().map { a3 -> af().map { a4 -> 
    val num = fl[a1](bs[0]!!) + fl[a2](bs[1]!!) + fl[a3](bs[2]!!) + fl[a4](bs[3]!!)
    val p = listOf( a1, a2, a3, a4 ).map { 
      if( it == 0 ) "+" 
      else "-"
    }.zip( bs ).map { 
      val (op, nu) = it
      listOf( "${op}", "${nu}" )
    }.flatten()
    
    val p2 = p.slice(1..p.size-1)
    results.add( Pair(num, p2) )
  } } } } 
  //println(results)
  results.filter { 
    val (k,v) = it
    k == 7
  }.first().let { 
    val (k, v) = it 
    println( v.joinToString("") + "=7" )
  }
}
