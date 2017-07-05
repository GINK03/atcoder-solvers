
fun main( args : Array<String> ) { 
  val n = readLine()
  val pat = readLine()!!
    .split(" ")
    .map { it.toInt() }  
    .map { 
      when {
        1 <= it    && it <= 399 -> "hai"
        400 <= it  && it <= 799 -> "cha"
        800 <= it  && it <= 1199 -> "midori"
        1200 <= it && it <= 1599 -> "mizu"
        1600 <= it && it <= 1999 -> "ao"
        2000 <= it && it <= 2399 -> "ki"
        2400 <= it && it <= 2799 -> "tou"
        2800 <= it && it <= 3199 -> "aka"
        3200 <= it               -> "what"
        else -> null
      }
    }

  val whsize = pat.filter { it == "what" }.size
  val nokori = listOf("hai", "cha", "midori", "mizu", "ao", "ki", "tou", "aka").filter {
                  !pat.contains(it)
                }
  val choised= pat.filter { it != "what"}.toSet().size
  val padsize= choised + when { whsize  <= nokori.size -> { whsize }; else -> nokori.size } 
  println("$choised $padsize")
}
