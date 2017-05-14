fun main(args: Array<String>) {
  val base = "WBWBWWBWBWBWWBWBWWBWWBWBWWBWBWBWWBWBWWBW"
  val t    = readLine()!!
  val a    = mapOf( 0 to "Do", 2 to "Re", 4 to "Mi", 5 to "Fa", 7 to "So", 9 to "La", 11 to "Si" )
  for( i in (0..19) ) { 
    val ev = base.slice(i..i+19)
    if(ev == t) {
      println("${a[i]}")
      break
    }
  }
}
