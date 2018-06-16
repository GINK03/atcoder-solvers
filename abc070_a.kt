
fun main(args:Array<String>) {
    val n = readLine()!!
    val r = n.reversed()
    when( n == r ) { true -> "Yes"; else -> "No" }.run(::println)
}
