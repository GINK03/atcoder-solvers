
fun main(args:Array<String>) {
  readLine()!!.toList().filter { it == 'o' }.size.let{ println(it*100+700) }
}
