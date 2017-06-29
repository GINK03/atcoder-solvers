
fun main( a : Array<String>) {
  var buff   = ""
  var stores = mutableListOf<String>()
  val text   = readLine()!!
  var state  = text.toList()[0]
  text.toList().mapIndexed { i, c ->
    when { 
      state != c -> {
        stores.add( buff )
        buff  = c.toString()
        state = c
        if( i == text.length-1 ) 
          stores.add( buff )
      }
      state == c -> { buff += c.toString()  }
    }
  }
  stores.map { st ->
    val first = st.toList().first().toString()
    val len   = st.length
    "$first$len"
  }.joinToString("")
  .let { println(it) }
}
