
fun main(args:Array<String>) {
  val (n,a,b) = readLine()!!.split(" ").map { it.toLong() }
  (1..n).map { each ->
    val sum = each.toString().map { char ->
      char.toString().toLong()
    }.sum()
    when { 
      a <= sum && sum <= b -> each
      else -> 0
    }
  }.sum().let {
    println(it)
  }
}
