
fun main(args:Array<String>) {
  val n = readLine()!!
  val s = readLine()!!.toList().map{ it.toString() }
  
  val max = s.size - 1
  var c = (s.size - 1)/2
  var p = 0 

  val scanned = mutableSetOf<Int>()

  val ans = mutableSetOf<Int>()
  while(true) {
    val left = (p+c)/2
    val lefta = s.slice(0..left-1).filter { it == "W" }.size + s.slice(left+1..max).filter { it == "E" }.size
    val right = (c+max)/2 
    val righta = s.slice(0..right-1).filter { it == "W" }.size + s.slice(right+1..max).filter { it == "E" }.size 
    
    val next = when {
      lefta >= righta -> right
      else -> left
    }
    if( next == c ) break
    //p = c
    c = next
    scanned.add(c)
    ans.add( lefta )
    ans.add( righta )
    //println("${lefta} ${righta} ${next} ${c} ${left} ${right}")
  }
  ans.min()!!.let(::println)
}
