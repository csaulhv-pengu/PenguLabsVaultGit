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
# First project (Hello world)
As example, project creation is as follows:

**Execution in bash:**
Please execute this command inside the directory that you want to contains your project.
```bash
cargo new hello_world
```

## Project general structure
Cargo will automatically create this structure:

hello_world/ <-- Project "root" folder
	|- Cargo.toml <-- Project configuration and dependencies
	|- src/
		|- main.rs <-- Key file

In next videos we will see further details.
## Inside main.rs
Rust will automatically generate a hello_world example:
```rust
fn main() {
	println!("Hello, World!")
}
```

main.rs file is always the first code to be executed when a rust project is run.

**To execute our first "Hello, World!" we need to:**
Please execute this command inside the directory that contains your cargo project (in this example: hello_world/)
```bash
cargo run
```

