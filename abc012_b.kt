
fun main( args : Array<String> ) {
  val a = readLine()!!.toInt()
  val h = a/3600
  val m = a/60 - a/3600*60
  val s = a%60
  println("%02d:%02d:%02d".format(h,m,s))
}
