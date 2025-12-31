---
Language: Rust
Author: PenguLabs
---

```
dHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHb
HHP%%#%%%%%%%%%%%%%%%%#%%%%%%%#%%VHH
HH%%%%%%%%%%#%v~~~~~~\%%%#%%%%%%%%HH
HH%%%%%#%%%%v'        ~~~~\%%%%%#%HH
HH%%#%%%%%%v'dHHb      a%%%#%%%%%%HH
HH%%%%%#%%v'dHHHA     :%%%%%%#%%%%HH
HH%%%#%%%v' VHHHHaadHHb:%#%%%%%%%%HH
HH%%%%%#v'   `VHHHHHHHHb:%%%%%#%%%HH
HH%#%%%v'      `VHHHHHHH:%%%#%%#%%HH
HH%%%%%'        dHHHHHHH:%%#%%%%%%HH
HH%%#%%        dHHHHHHHH:%%%%%%#%%HH
HH%%%%%       dHHHHHHHHH:%%#%%%%%%HH
HH#%%%%       VHHHHHHHHH:%%%%%#%%%HH
HH%%%%#   b    HHHHHHHHV:%%%#%%%%#HH
HH%%%%%   Hb   HHHHHHHV'%%%%%%%%%%HH
HH%%#%%   HH  dHHHHHHV'%%%#%%%%%%%HH
HH%#%%%   VHbdHHHHHHV'#%%%%%%%%#%%HH
HHb%%#%    VHHHHHHHV'%%%%%#%%#%%%%HH
HHHHHHHb    VHHHHHHH:%odHHHHHHbo%dHH
HHHHHHHHboodboooooodHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
VHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHV
```
---
# Variables
## What is a variable?
A variable is a name that points to a specific value in memory.
For rust, it is declared using reserved word: "let"

```rust
let x = 5;
```

![[Pasted image 20251230213606.png]]

---
## Immutability
Variables are inmutables by defect.
	Which means that a variable cannot change its value after assignation.

This code will gave you and error during compiling process:
```rust
let x = 5;
x = 6;
```
"Cannot assign twice to immutable variable."

### Why does Rust makes this?
- It helps to prevent errors
- Makes code more predictable (you know that that variable cannot change value during execution)

---
## Mutability
If you want to have a mutable variable, you need to make it clear in this way:
```rust
let mut x = 5;
x = 6;
```

**Key idea:**
- Let <-- no change
- Let mut <-- can change

---
# Types of DATA
In Rust there are no types of variables, but types of data.
Type of data is not a property of the variable, it is a property of the value that the variable contains.

Variables are only:
- Mutable
- Immutable

Types of data (primitive):
- **Integer**

| Type | Bits | Signed | Unsigned |
| ---- | ---- | ------ | -------- |
| 8    | i8   | i8     | u8       |
| 16   | i16  | i16    | u16      |
| 32   | i32  | i32    | u32      |
| 64   | i64  | i64    | u64      |
| 128  | i128 | i128   | u128     |
	- i8 range (-128 < i8 < 127)
	- u8 range (0 < u8 < 255)

- **Float (f64)**
	- Range (-1.8x10³⁰⁸ < f64 < 1.8x10³⁰⁸)
	- Minimum positive number (not zero): 2.2 x 10⁻³⁰⁸
- **Boolean (bool)**
	- True
	- False
- **Char (char)**
	- a
	- b
	- c
- **Strings (String, &str)**
	- abcdf
	- asd1231!%
	- &str: immutable
	- string: mutable
# Examples:

```rust
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
```

