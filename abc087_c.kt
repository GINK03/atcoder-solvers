
fun main(args:Array<String>) {
  val n = readLine()!!
  val ls = (1..2).map { 
    readLine()!!.split(" ").map(String::toInt)
  }
  val width = ls.first().size
  (0..width-1).map { 
    ls[0].slice(0..it).sum() + ls[1].slice(it..width-1).sum()
  }.max()!!.let(::println)
}
