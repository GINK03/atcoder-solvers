
fun main( args : Array<String> ) { 
  val len = readLine()!!.toInt()
  val cen = len/2 + 1
  val txt = readLine()!!.toList().map { x -> x.toString() }

  val head = txt.slice(0..cen-2).reversed()
  val tail = txt.slice(cen..txt.size-1)
  val zip  = head.zip(tail)
  val ans  = listOf( Pair("a", "c"), Pair("c", "a"), Pair("b", "b") )
  val st = zip.mapIndexed { i, x ->
    when { 
      i%3 == 0 -> x == ans[0]
      i%3 == 1 -> x == ans[1]
      i%3 == 2 -> x == ans[2]
      else ->  null
    }
  }
  when { 
    txt.size%2 == 0           -> println( -1 )
    txt[cen-1] != "b"         -> println( -1 )
    st.all { x -> x == true } -> println( st.size )
    else                      -> println( -1 )
  }
}
