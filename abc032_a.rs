use std::io::{self, Read};
use std::io::prelude::*;
use std::collections::BTreeSet;
use std::collections::HashSet;
use std::collections::HashMap;

fn main(){
  let stdin  = std::io::stdin();
  let mut it = stdin.lock().lines();
  let mut s:HashSet<char> = HashSet::new();
  let mut m:HashMap<String,f64> = HashMap::new();

  let a    = &it.next().unwrap().unwrap();
  let a    = a.parse::<i64>().unwrap();
  let b    = &it.next().unwrap().unwrap();
  let b    = b.parse::<i64>().unwrap();
  let c    = &it.next().unwrap().unwrap();
  let mut c = c.parse::<i64>().unwrap();
  loop {
    if c%a == 0 && c%b ==0 {
      break;
    } else {
      c = c + 1;
    }
  }
  println!("{}", c)


}

