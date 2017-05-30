use std::io::{self, Read};
use std::io::prelude::*;

fn main(){
  let stdin  = std::io::stdin();
  let mut it = stdin.lock().lines();
  let a      = &it.next().unwrap().unwrap();
  let a      = a.split(" ")
   .collect::<Vec<_>>()
   .iter()
   .map( |&x| {
     return x.parse::<i64>().unwrap();
   })
   .collect::<Vec<i64>>();
   if a[0] < a[1] {
     println!("Better")
   } else {
     println!("Worse")
   }
}
