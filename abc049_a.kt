
fun main(args : Array<String> ) {
  val c = readLine()!!.toList()[0]
  when( listOf('a', 'e', 'i', 'o', 'u').contains(c) ) {
    true  -> println("vowel")
    false -> println("consonant")
  }
}
