
fun main(args : Array<String>) { 
  val n = readLine()!!.toInt()
  var r = 0
  for( i in (1..n) ) { 
    r += i
  }
  println(r)
}
