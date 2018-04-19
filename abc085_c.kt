
fun main(args:Array<String>) {
  val (n,y2) = readLine()!!.split(" ").map{ it.toInt() }
  val y = y2

  val man = y/10000
  val gsn = y%10000/5000
  val sen = y%5000/1000
  val sum = listOf(man, gsn, sen).sum()
  when { 
    sum > n -> println("-1 -1 -1")
    else -> {
      val mm = y/10000
      val gg = y/5000
      val ss = y/1000

      var stack = mutableListOf<Int>()
      scan@for( m in (mm downTo 0) ) {
        for( g in (gg downTo 0) ) {
          for( s in (ss downTo 0) ) {
            if( m + g + s == n &&  m*10000 + g*5000 + s*1000 == y2) {
              stack = mutableListOf<Int>( m, g, s )
              break@scan
            }
          }
        }
      }
      println( stack.map{ it.toString() }.joinToString(" ") )
    }
  }
}
