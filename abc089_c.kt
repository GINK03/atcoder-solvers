
fun main(args:Array<String>){
  val march = "MARCH".toList().map(Char::toString).toSet()

  val n = readLine()!!.toInt()
  val bs = (1..n).map { readLine()!!.toList().first().toString() }

  val char_freq = mutableMapOf<String, Int>()

  for( char in bs ) {
    if( march.contains(char) == false )
      continue
    if( char_freq.get(char) == null )
      char_freq[char] = 0
    char_freq[char] = char_freq[char]!! + 1
  }

  //println(char_freq)
  val size = char_freq.size
  
  // 3つ選んだアルファベットのsetを作る

  val bag = mutableSetOf<MutableSet<String>>()

  val keys = char_freq.toList().map { it.first }

  for( key1 in keys ) {
    for ( key2 in keys ) {
      for( key3 in keys ) {
        val minibag = mutableSetOf<String>()
        minibag.add(key1)
        minibag.add(key2)
        minibag.add(key3)
        if( minibag.size != 3) continue
        bag.add(minibag)
      }
    }
  }
  bag.map {  minibag ->
    minibag.map { key ->
      char_freq[key]!!
    }.reduce { y,x -> y*x }
  }.sum().let(::println)
}
