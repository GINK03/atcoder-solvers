
fun main(args: Array<String>) { 
  val (a,b,c,d) = readLine()!!.split(" ").map { x ->
    x.toDouble()
  }
  when { 
    b/a > d/c -> println("TAKAHASHI")
    b/a == d/c-> println("DRAW")
    else      -> println("AOKI")
  }
}
