
fun main(args: Array<String>) { 
  val (t1, t2) = readLine()!!.split(" ").map { x -> 
    x.toInt() 
  }
  println( listOf( (t1+1)*t2, t1*(t2+1) ).max()  )
}
