fun main(args:Array<String>) {
  val (a, b, k) = readLine()!!.split(" ").map(String::toLong)

  val ins = (a..listOf(a+k-1,b).min()!!).toSet() + (listOf(b-k+1,a).max()!!..b).toSet() 

  ins.toList().sorted().map(::println)
}
  
