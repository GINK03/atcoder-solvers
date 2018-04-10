
fun main(args:Array<String>) {
  val (m,n) = readLine()!!.split(" ").map(String::toLong)
  when {
    m == 1L && n == 1L -> 1L
    m == 1L && n != 1L -> n - 2  
    m != 1L && n == 1L -> m - 2
    else -> (m-2L)*(n-2L)
  }.let (::println)
}
