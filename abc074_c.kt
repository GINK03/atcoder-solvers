
fun main( args:Array<String> ) {
  val xs = readLine()!!.split(" ").map(String::toInt)
  val a = xs[0]
  val b = xs[1]
  val c = xs[2]
  val d = xs[3]
  val e = xs[4]
  val f = xs[5]
  (0..10).map { a_num -> 
    (0..10).map { b_num -> 
      // Cを入れるとき
      val water = a_num*100 + b_num*100
      (0..(f-water)/c).map { c_num ->
        (0..(f-water)/d).map { d_num ->
          listOf(a_num, b_num, c_num, d_num)
        }
      }.flatten()
    }.flatten()
  }.flatten().mapNotNull { 
    val (a_num, b_num, c_num, d_num) = it
    val water = a_num*100 + b_num*100
    val sugar = c*c_num + d*d_num 
    when { 
      water + sugar > f -> null
      sugar.toDouble()/(water+sugar) > e.toDouble()/(100+e) -> null
      else -> Triple( water, sugar, 100*sugar.toDouble()/(water+sugar) )
    }
  }.filter { it.first != 0 && !it.third.isNaN() }.let { 
    //println(it)
    val max = it.maxBy { it.third }!!.third
    it.filter { it.third == max } 
  }.run(::println)
}
