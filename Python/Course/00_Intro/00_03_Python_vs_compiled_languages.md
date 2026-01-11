---
Language: Python
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

Machines language is binary (0s and 1s)
	The lowest-level language
	Pure binary instructions
	Directly executed by the CPU

All programs must be translated before running.
	A translation step is always needed

# Two main translation approaches
## Compilation
1. Write source code (C, C++, Rust)
2. Compile the code
3. Generate machine code
4. Run the executable

- Translation happens **before** execution
- Errors are found early
- The result is a standalone program
## Interpretation
1. Write source code (Python)
2. Start the interpreter
3. Interpreter reads code line by line
4. Code is executed immediately

- Translation happens **while** running
- No separate compile step
- Errors are found during execution
## Comparison
![[Pasted image 20260103185250.png]]
## Why this matters?
- Affects performance
	- Interpreted languages are slower than compiled ones in complicated tasks
	- Affect error handling

## What matters right now
- You don’t need to memorize details
- Just remember: translation always exists
- Different languages choose different paths