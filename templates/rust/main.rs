use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let output = solve(&input);
    print!("{output}");
}

fn solve(_input: &str) -> String {
    // TODO: solve the problem
    String::new()
}
