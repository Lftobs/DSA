fn main() {
    let str = "racecar";
    let (mut x, mut y) = (0, str.len() - 1);
    println!("x: {}, y: {}", x, y);
    
    while x <= y {
        if str.chars().nth(x) != str.chars().nth(y) {
            println!("false");
            break;
        };
        if x == y && str.chars().nth(x) == str.chars().nth(y) {
            println!("true");
            break;
        };
        x += 1;
        y -= 1;
    }
    
}
