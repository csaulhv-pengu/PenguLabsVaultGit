- **Integers**
	- Supports + - * / %
	- Int/Int does not get you any decimals.
- **Float**
	- Sames as integers but with decimals in results
- **Boolean**
	- Logic operators
	- && AND
	- || OR
	- ! Negative
- **Char**
	- It represents a single one Unicode character
	- It can be compared with other chars
- **&str**
	- Immutable
	- Can be combined with format!
- **String**
	- Mutable
	- Allows push, push_str and concatenation with +


```rust
fn main() {
    // =====================
    // Enteros con signo (i32)
    // =====================
    let a: i32 = 10;
    let b: i32 = 3;
    
    println!("i32 sum: {}", a + b);        // suma
    println!("i32 sub: {}", a - b);        // resta
    println!("i32 mul: {}", a * b);        // multiplicación
    println!("i32 div: {}", a / b);        // división entera (resultado truncado)
    println!("i32 mod: {}", a % b);        // residuo (módulo)
    
    // =====================
    // Enteros sin signo (u32)
    // =====================
    let x: u32 = 20;
    let y: u32 = 6;
    
    println!("u32 sum: {}", x + y);
    println!("u32 sub: {}", x - y);
    println!("u32 mul: {}", x * y);
    println!("u32 div: {}", x / y);
    println!("u32 mod: {}", x % y);
    
    // =====================
    // Flotantes (f64)
    // =====================
    let p: f64 = 5.0;
    let q: f64 = 2.0;
    
    println!("f64 sum: {}", p + q);
    println!("f64 sub: {}", p - q);
    println!("f64 mul: {}", p * q);
    println!("f64 div: {}", p / q); // división real
    
    // =====================
    // Booleanos (bool)
    // =====================
    let is_ready: bool = true;
    let is_admin: bool = false;
    
    println!("AND: {}", is_ready && is_admin); // AND lógico
    println!("OR: {}", is_ready || is_admin);  // OR lógico
    println!("NOT: {}", !is_ready);             // negación
    
    // =====================
    // Caracteres (char)
    // =====================
    let letter: char = 'A';
    
    // Los char no se suman directamente, pero pueden compararse
    println!("Is letter 'A'? {}", letter == 'A');
    println!("Is letter different from 'B'? {}", letter != 'B');
    
    // =====================
    // &str (string literal)
    // =====================
    let hello = "Hello";
    let world = "World";
    
    // No se pueden unir directamente con +
    let message = format!("{} {}", hello, world);
    println!("{}", message);
    
    // =====================
    // String (heap allocated)
    // =====================
    let mut name = String::from("Rust");
    
    name.push(' ');              // agregar un char
    name.push_str("Lang");       // agregar &str
    println!("Name: {}", name);
    
    // Concatenación con +
    let full = name + " Rocks!";
    println!("{}", full);
}
```