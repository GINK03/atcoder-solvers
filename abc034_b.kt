
fun main(args : Array<String>) {
  val a = readLine()!!.toLong()
  when {
    a%2L == 0L -> {
      println(a-1)  
    }
    else -> {
      println(a+1)
    }
  }
}
