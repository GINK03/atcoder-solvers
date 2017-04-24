import java.math.BigDecimal


fun main(args: Array<String>) {
  val a = BigDecimal(readLine())
  val b = BigDecimal(readLine())
  if( a > b ) { 
    println("GREATER")
  } 
  if( a < b ) {
    println("LESS")
  }
  if( a == b ) {
    println("EQUAL")
  }
}
