
fun main( args : Array<String> ) {
  val (n, a, b) = readLine()!!.split(" ").map { it.toInt() }
  val ns = (1..n).map { readLine()!!.toInt() }
  var stat = ns.first()
  val ss = ns.mapIndexed {  i, x ->
    when {
       i == 0 -> { a <= x && x <= b }
       else   -> { val r =  a <= x + stat && x + stat <= b 
                   stat += x
                   r
                 }
    }
  }
  println( ss.count { it == true }  )
}
