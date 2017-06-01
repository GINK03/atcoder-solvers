
fun main(args : Array<String>) {
  val a = readLine()!!.toInt()
  val b = readLine()!!.toInt()
  var c = readLine()!!.toInt()
  while (true) {
    if (  c%a == 0 && c%b == 0 ) 
      break
    else 
      c = c + 1
  }
  println(c)
}
