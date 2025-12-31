fn main() {
    // =====================
    // Signed integers (i32)
    // =====================
    let a: i32 = 10;
    let b: i32 = 3;
    
    println!("i32 sum: {}", a + b);
    println!("i32 sub: {}", a - b);
    println!("i32 mul: {}", a * b);
    println!("i32 div: {}", a / b);
    println!("i32 mod: {}", a % b);
    
    // =====================
    // Unsigned integer (u32)
    // =====================
    let x: u32 = 20;
    let y: u32 = 6;
    
    println!("u32 sum: {}", x + y);
    println!("u32 sub: {}", x - y);
    println!("u32 mul: {}", x * y);
    println!("u32 div: {}", x / y);
    println!("u32 mod: {}", x % y);
    
    // =====================
    // Float (f64)
    // =====================
    let p: f64 = 5.0;
    let q: f64 = 2.0;
    
    println!("f64 sum: {}", p + q);
    println!("f64 sub: {}", p - q);
    println!("f64 mul: {}", p * q);
    println!("f64 div: {}", p / q); // división real
    
    // =====================
    // Booleans (bool)
    // =====================
    let is_ready: bool = true;
    let is_admin: bool = false;
    
    println!("AND: {}", is_ready && is_admin); // AND lógico
    println!("OR: {}", is_ready || is_admin);  // OR lógico
    println!("NOT: {}", !is_ready);             // negación
    
    // =====================
    // Character (char)
    // =====================
    let letter: char = 'A';
    
    // Char cannot be conncatenated as a sum(+)
    // Chars can be compared
    println!("Is letter 'A'? {}", letter == 'A');
    println!("Is letter different from 'B'? {}", letter != 'B');
    
    // =====================
    // &str
    // =====================
    let hello = "Hello";
    let world = "World";
    
    // Char cannot be conncatenated as a sum(+)
    let message = format!("{} {}", hello, world);
    println!("{}", message);
    
    // =====================
    // String (heap allocated)
    // =====================
    let mut name = String::from("Rust");
    
    name.push(' ');              // Adding a char
    name.push_str("Lang");       // Assing a &str
    println!("Name: {}", name);
    
    // Concatenación con +
    let full = name + " Rocks!";
    println!("{}", full);
}