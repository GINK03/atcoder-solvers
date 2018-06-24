
fun main(args:Array<String>) {
  var x = readLine()!!
  "aiueo".toList().map(Char::toString).map { x = x.replace(it, "") }
  println(x)
}
