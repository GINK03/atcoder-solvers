import java.lang.Math
fun main(args:Array<String>) {
  val n = readLine()
  var xs = readLine()!!.split(" ").map(String::toInt).mapIndexed { index, e -> e - index -1 }.sorted()

  val median:Double =  xs.sorted().let { (it[it.size / 2].toDouble() + it[(it.size - 1) / 2]).toDouble() / 2 }

  setOf(median.toInt(), median.toInt()+1).map { med -> xs.map{ Math.abs(it - med) }.sum() }.min()!!.run(::println)
}
