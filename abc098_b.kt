
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  val s = readLine()!!
  
  val set1 = mutableSetOf<Int>()
  for( i in (0..n-1) ) {
    //println("${s.slice(0..i).toSet()}, ${s.slice(i+1..n-1).toSet()}" )
    val f1 = s.slice(0..i).toSet()
    val f2 = s.slice(i+1..n-1).toSet()
    set1.add( f1.intersect(f2).size )
  }
  set1.max().let(::println)
}
