
fun main(args:Array<String>) {
  val n = readLine()
  var ins = readLine()!!.split(" ").map(String::toLong)

  var c = 0
  while(true) {
    if( ! ins.all { it%2L == 0L } ) break
    c += 1
    ins  = ins.map { it/2L }
  }
  println(c)
}
