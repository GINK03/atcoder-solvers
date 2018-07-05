
fun main(args:Array<String>) {
  val (d, N) = readLine()!!.split(" ").map(String::toInt)
  var c = 1
  val bu = mutableListOf<Int>()
  val dd = when(d) {0 -> 1;1 -> 100;2 -> 100000;else -> null}!!

  ((N-(N-1)/99)*dd).run(::println)
  // cheating from https://img.atcoder.jp/abc100/editorial.pdf
}

  
