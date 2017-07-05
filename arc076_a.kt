import java.math.BigDecimal

fun main( args : Array<String> ) {
  val bbb   = BigDecimal(1000000007L)
  val (a,b) = readLine()!!.split(" ").map { it.toInt() }
  val A     = listOf(BigDecimal(1), (1L..a).map { BigDecimal(it) }. reduce {y,x -> 
                    y.rem(bbb).times(x.rem(bbb)).rem(bbb)
                  } ).max()!!
  val B     = listOf(BigDecimal(1), (1L..b).map { BigDecimal(it) }.reduce {y,x -> 
                    y.rem(bbb).times(x.rem(bbb)).rem(bbb)
                  } ).max()!!
  println(A) 
  when {
    a == b -> A.times(B).rem(bbb)
    a+1 == b || a == b+1 -> A.times(B).rem(bbb)
    else -> 0
  }.let { println(it) }
}
