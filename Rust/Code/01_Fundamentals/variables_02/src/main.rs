fn main() {
	// You can define data without specification of what data type it will contain.
	// Rust automatically consider a data type.
	let x = 5; // i32
	println!("x = {}",x);
	
	let mut y = 3.14; //f64
	y = 2.6;
	println!("y = {}", y);
	
	let z = true; //bool
	println!("z = {}", z);
	
	// You can be explicit on the data type you want.
	let a: i32 = -100;
	let b: u32 = 42;
	let c: f64 = 3.14159;
	
	println!("a = {}", a);
	println!("b = {}", b);
	println!("c = {}", c);
	
	//boolean
	let is_active: bool = true;
	println!("is_active = {}", is_active);
	
	//char
	let letter: char = 'A';
	println!("letter = {}", letter);
	
	// &str y string
	let greeting = "Hello"; // &str (string literal)
	let mut name = String::from("Rust");
	
	name.push_str(" Lang"); // Adding more characters to a string
	println!("{} {}", greeting, name);
}