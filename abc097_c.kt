
fun main(args:Array<String>) {
  val str = readLine()!!
  val n = readLine()!!.toInt()

  val strs = mutableSetOf<String>()
  for( s in (0..str.length-1) ) {
    for( e in (0..str.length-1) ) {
      strs.add( str.slice(s..e) )
    }
  }

  val strs2 = strs.filter { it != "" }.toList().sorted()
  println(strs2[n-1])
  
}
