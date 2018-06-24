
fun main(args:Array<String>) {
  val (n, h) = readLine()!!.split(" ").map(String::toInt)

  val (a, b, c, d, e) = readLine()!!.split(" ").map(String::toInt)

  val bb = mutableListOf<Triple<Int,Int,Int>>()
  for( k in (0..n) ) {
    for( i in (0..n-k) ) {
      for( l in (0..n-i-k) ) {
        if( k+i+l == n && b*k + d*i - e*l + h > 0 ) bb.add( Triple(k, i, l) ) 
      }
    }
  }
  //println(bb)
  bb.map { 
    val (a1, a2, a3) = it
    a*a1+c*a2
  }.min().run(::println)
}
