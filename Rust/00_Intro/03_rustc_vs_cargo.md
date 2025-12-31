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
# rustc vs cargo
## rustc
- "rustc" es Rust's compiler.
- It is use to compile one single Rust file (.rs)

Sintaxis:
Executed in the same path as your .rs file
```bash
rustc main.rs
```

- Advantages:
	- Fast and simple for quick and small examples
- Disadvantages:
	- It cannot handle dependencies neither big projects easily

---
## cargo
- "cargo" is the official tool for project's management in Rust.
- It allows to:
	- Create projects
	- Manage dependencies
	- Compilation and execution
	- Make test and benchmarks

Sintaxis:
```bash
# Project creation
cargo new my_project_name
# Change to project's directoy
cd my_project
# Compile and execute code
cargo run
```

- Advantages:
	- Ideal for real projects
	- Flow automatically managed
- Disadvantages:
	- ¿?