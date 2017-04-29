
fun main(args:Array<String>) {
  val (a, b) = readLine()!!.split(" ")
  when(a) {
    "H" -> { 
      when(b) {
        "H" -> println("H")
        "D" -> println("D")
      }
    }
    "D" -> {
      when(b) {
        "H" -> println("D")
        "D" -> println("H")
      }
    }
  }
}
