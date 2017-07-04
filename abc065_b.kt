
data class A(var param: Boolean, val target: Int)
fun main( args : Array<String> ) {
  val n  = readLine()!!.toInt()
  val ba = (1..n).map {
    A(false, readLine()!!.toInt() - 1)
  }
  var cur = 0
  for( i in (1..n) ) {
    if( cur == 1 ) {
      println(i-1)
      break
    }else if( ba[cur].param == true ) {
      println(-1)
      break
    }
    ba[cur].param = true
    cur = ba[cur].target
  }
}
