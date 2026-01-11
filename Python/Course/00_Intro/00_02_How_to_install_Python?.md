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

# How to install Python?
Python can be installed in different ways. But we will use Miniconda.
URL: https://www.anaconda.com/docs/getting-started/miniconda/main

Please install **MINICONDA** NO **ANACONDA**
- It includes Python
- Includes environment manager
- MINIconda is lightweight than Anaconda
- Cross-platform
	- Please follow install instructions for your Operative System

![[Pasted image 20260103183611.png]]
## Why environments matter?
- Different projects need different versions (of Python or some module)
- Avoid dependency conflicts
- Clean and reproducible setups
![[Pasted image 20260103212424.png]]

## Creating a Python environment
We will use Python version 3.12 because it is stable.
```bash
conda create -n python_course python=3.12
conda activate python_course
```

## Hello world
```python
print("Hello world!")
```