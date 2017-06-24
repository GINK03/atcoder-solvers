import java.util.*
data class A(var x:Int, var type:Boolean)
fun main(args : Array<String> ) { 
  readLine()

  val bs = readLine()!!
            .split(" ")
            .toList()
            .map { x -> x.toInt() }
 
  val ts = (0..bs.size-1).map{ i ->
    val cs     = bs.map { x -> A(x, false) }
    cs[i].type = true
    cs
  }
  ts.map{ vs ->
    val zs = (0..vs.size-1).map { i ->
      val xs = vs.map{ x -> x.copy()}
      xs[i].type = true
      xs
    }.filter { xs ->
      xs.count { x -> x.type == true } == 2
    }
    println( zs )
    zs
  }

  println( ts )
}
