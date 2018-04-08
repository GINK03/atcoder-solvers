
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  val ms = readLine()!!.split(" ").map(String::toInt)

  val num_freq = mutableMapOf<Int, Int>()
  ms.map { num -> 
    if( num_freq.get(num) == null ) 
      num_freq[num] = 0
    num_freq[num] = num_freq[num]!! + 1
  }
  //println(num_freq)

  // 全部取り除くべき人か
  // 一部取りのぞくか

  var remove = 0
  num_freq.toList().map { kv -> 
    val (num, freq) = kv
    if( num <= freq )
      remove += freq - num
    else
      remove += freq
  }
  println( remove)
}
