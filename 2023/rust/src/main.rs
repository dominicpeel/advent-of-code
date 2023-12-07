use clap::Parser;

#[derive(Debug, Parser)]
struct Args {
    day: usize,
}

fn main() {
    let args = Args::parse();
    println!("Day {}!", args.day);
}

