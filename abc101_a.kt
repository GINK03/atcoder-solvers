
fun main(args:Array<String>){
  readLine()!!.toList().map{ when{ it == '+' -> 1 else -> -1 } }.sum().run(::println)
}
