
fun main(args : Array<String>) {
  val (sx, sy, tx, ty) = readLine()!!.split(" ").map {x -> x.toInt()} 
  println( "U".repeat(ty - sy) + "R".repeat(tx - sx) + "D".repeat( ty - sy ) + "L".repeat(tx - sx) + 
            "L" + "U".repeat(ty - sy + 1) + "R".repeat(tx - sx + 1)  + "D" + 
            "R" + "D".repeat(ty - sy + 1) + "L".repeat(tx - sx + 1)  + "U")
}
