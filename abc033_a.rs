
use std::io::{self, Read};
use std::io::prelude::*;
use std::collections::BTreeSet;
use std::collections::HashSet;

fn main(){
  let stdin  = std::io::stdin();
  let mut it = stdin.lock().lines();
  //let mut bs = BTreeSet::new();
  let mut s:HashSet<char> = HashSet::new();

  let a      = &it.next().unwrap().unwrap();
  for b in a.chars() {
    let c = &b;
    s.insert(c.clone());
  }
  let l = s.len();
  let t =  match l {
    1 => println!("SAME"),
    _ => println!("DIFFERENT"),
  };
}

