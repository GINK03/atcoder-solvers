

var effector = 1
fun divisorGenerator(n:Long):List<Long> { 
  val large_divisors = mutableListOf<Long>()
  for( i in (effector..(Math.sqrt(n.toDouble()) + 1).toInt() ) ) {
    if( n % i == 0L) { 
      large_divisors.add( i.toLong() ) 
      large_divisors.add( n / i)
    }
  }
  effector = (Math.sqrt(n.toDouble()) + 1).toInt() 
  return large_divisors.toSet().sorted()
}
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  
  var effect = 1L
  (1..n).map { 
    effect = ( it*effect ) 
    val r = divisorGenerator(effect)
    r
  }.flatten().toSet().toList().sorted().size.run(::println)
}
