import java.lang.*

fun main(args:Array<String>) {
  val bm = (0.."11111".toInt(2)).map {
    "${java.lang.Integer.toBinaryString(it)}".padStart(5, '0')
  }.filter {
    it.toList().filter { it == '1' }.size == 3
  }
  //println(bm)

  val n = readLine()!!.toInt()
  val m = mutableMapOf<String, Int>()
  val march = "MARCH".toList().map { it.toString() }
  for( it in (1..n) ) { 
    val name = readLine()!!
    val h = name[0].toString()
    if( !march.contains(h) )
      continue
    if( m.get(h) == null )
      m[h] = 0
    m[h] = m[h]!! + 1
  }

  val marchFreq = "MARCH".toList().map { char ->
    val h = char.toString()
    when {
      m.get(h) != null -> Pair(h,m[h]!!) 
      else -> Pair(h,0)
    }
  }

  var result = 0
  for( mask in bm ) {
    val comb = mask.toList().zip( marchFreq ).map {
      val (bit, pair) = it
      val freq = pair.second
      //println("${bit.toString().toInt()} ${freq}")
      bit.toString().toInt()*freq 
    }.filter { it != 0 }
    if( comb.size == 3 ) {
      val min_result = comb.reduce { y,x -> y*x }
      result += min_result
      //println("${mask} ${marchFreq} ${comb} ${min_result}" )
    }
  }
  println(result)
}
