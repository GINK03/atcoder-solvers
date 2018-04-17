
fun main(args:Array<String>){
  val (n,m,x) = readLine()!!.split(" ").map(String::toInt)

  val ns = (0..n).map { 0 }.toMutableList()

  val cs = readLine()!!.split(" ").map(String::toInt).map { ns[it] = 1 }

  listOf(ns.slice(x..ns.size-1).sum(), ns.slice(0..x).sum()).min().let(::println)
}
