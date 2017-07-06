
val store : MutableList<MutableList<Int>> = mutableListOf()

fun perm(ss:MutableList<Int>, buff:MutableList<Int>) {
  if( ss.size == 0 ) {
    store.add(buff)
    return
  }
    
  (0..ss.size-1).map { i ->
    val nextSs   = ss.toMutableList()
    val nextBuff = buff.toMutableList()
    val pop      = nextSs[i]
    nextBuff.add( pop )
    nextSs.removeAt(i)
    perm(nextSs, nextBuff)
  }
}


fun main( args : Array<String> ) {
  val n = readLine()!!.toInt()
  val ss = (1..n).map { 
    readLine()!!.toInt()
  }

  perm(ss.toMutableList(), mutableListOf<Int>() )
  val ans = mutableSetOf<Int>()
  store.toSet().map { xs ->
    for(i in (xs.size-1 downTo 0) ) {
      val x = xs.slice(0..i).reduce { y,x -> y+x }
      val a = when {
        x%10 == 0 -> 0
        else      -> x
      }
      ans.add( a )
    }
  }
  println( ans.max() )
}
