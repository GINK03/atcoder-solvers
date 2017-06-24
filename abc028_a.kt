
fun main(args : Array<String>) { 
  val x = readLine()!!.toInt()
  println( when {
    0  <= x && x <= 59 -> "Bad"
    60 <= x && x <= 89 -> "Good"
    90 <= x && x <= 99 -> "Great"
    else               -> "Perfect"
  } )
}
