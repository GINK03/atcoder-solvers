
fun main( args : Array<String> ) {
  val bs = readLine()!!
  for(i in (bs.length - 2 downTo 0) ) {
    val check = bs.slice(0..i)
    if( check.length % 2 == 1 ) continue
    if( check.slice(0..i/2) == check.slice(i/2+1..i) ) {
      println(check.length)
      break
    }
  }
}
