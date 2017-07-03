
fun main( args : Array<String> ) {
  val N  = readLine()!!.toInt()  
  val M  = N % 30
  val ta = (1..6).map { it }.toMutableList()
  (0..M-1).map { i ->
    val sw1 = (i%5 + 1 - 1)
    val sw2 = (i%5 + 2 - 1)
    val tmp = ta[sw2]
    ta[sw2] = ta[sw1]
    ta[sw1] = tmp
    if (ta == mutableListOf(1,2,3,4,5,6))
      print("$i $ta")
  }
  println( ta.joinToString("") )
}
