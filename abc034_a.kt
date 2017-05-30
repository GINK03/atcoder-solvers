
fun main(args : Array<String>) { 
  val (a, b) = readLine()!!.split(" ").map { x -> x.toInt() }
  when { 
    a < b -> println("Better")
    else  -> println("Worse")
  }
}
