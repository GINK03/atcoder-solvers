
fun main(args : Array<String> ) { 
  val r = readLine()!!.split(" ")
    .map { x -> 
      x.toList()[0]
    }.joinToString("")
  println(r)
}
