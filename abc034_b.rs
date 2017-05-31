use std::io::{self, Read};
use std::io::prelude::*;

fn main() {
  let stdin   = std::io::stdin();
  let mut it  = stdin.lock().lines();
  let a       = it.next().unwrap().unwrap(); 
  let a       = a.parse::<i64>().unwrap();
  if a % 2 == 0 {
    println!("{}", a - 1)
  } else {
    println!("{}", a + 1)
  }
}
