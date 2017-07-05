import java.math.BigDecimal

fun main( args : Array<String> ) {
  val bbb   = 1000000007L
  val (a,b) = readLine()!!.split(" ").map { it.toInt() }
  val A     = listOf(1L, (1L..a).map { it.toLong() }. reduce {y,x -> 
                    (y%bbb*x%bbb)%bbb
                  } ).max()!!
  val B     = listOf(1L, (1L..b).map { it.toLong() }.reduce {y,x -> 
                    (y%bbb*x%bbb)%bbb
                  } ).max()!!
  when {
    a == b -> (A%bbb*B%bbb)%bbb*2%bbb
    a+1 == b || a == b+1 -> (A%bbb*B%bbb)%bbb
    else -> 0
  }.let { println(it) }
}
