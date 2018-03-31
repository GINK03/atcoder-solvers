
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  val (d, x) = readLine()!!.split(" ").map { it.toInt() }

  (1..n).map { 
    ( (d-1) / readLine()!!.toInt() ) + 1
  }.sum().let{ println(it+x) }
}

