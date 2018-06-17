
fun main(args:Array<String>) {
  (0..10).map { 
    (0..it).map{ 2 }.reduce { y, x -> y*x } 
  }.toMutableList().let { m ->
    m.add(1)
    readLine()!!.toInt().let { n ->
      m.filter { n >= it }.maxBy { it }!!.run(::println)
    }
  }
}
