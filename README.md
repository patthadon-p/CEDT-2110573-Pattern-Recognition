# 📘 CEDT 2110573 Pattern Recognition - Homework Repository

This repository contains my cedt patt recog homework solutions written in **LaTeX**.  
It is structured for clarity, reproducibility, and ease of compilation.

---

## 📂 Repository Structure

```

.
│   
├── .venv/                      # Python virtual environment (if applicable)
│   
├── homework-01/
│   ├── main.tex                # LaTeX source file
│   ├── main.pdf                # Compiled homework
│   ├── code/                   # Any code snippets (if applicable)
│   │   ├── example-code-1.py
│   │   └── example-code-2.ipynb
│   └── images/                 # Diagrams / figures (if any)
│
├── templates/
│   └── homework-template.tex
├── CEDT-Homework-style.sty       # Styling
├── requirements.txt              # Python dependencies (if any)
├── .gtignore                     # Git ignore file
└── README.md

````

- **`homework-xx/`** → Each homework assignment with its LaTeX file and compiled PDF.  
- **`templates/`** → Common LaTeX macros, environments, or homework style templates. 
- **`code/`** → Any code snippets or Jupyter notebooks used for calculations or plots. 
- **`images/`** → Supporting figures, TikZ diagrams, or plots.  

---

## 🛠️ Requirements

To compile the `.tex` files into PDF, you’ll need:

- **LaTeX distribution** (e.g., [TeX Live](https://tug.org/texlive/), [MikTeX](https://miktex.org/), or Overleaf online)  
- Recommended packages:
  - `amsmath`, `amssymb` (math environments and symbols)
  - `enumitem` (custom lists)
  - `tcolorbox` (solution/problem boxes)
  - `tikz` (diagrams)

To compile the `.py` or `.ipynb` code snippets, you’ll need:
- **Python 3.x** with libraries listed in the `requirements.txt` (if applicable)
  - You can create a virtual environment and install dependencies via:
    ```bash
    python -m venv .venv/
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    ```
- **Jupyter Lab/Notebook** (if using `.ipynb` files)

---

## ▶️ Compilation

From the terminal:

```bash
cd homework-01
pdflatex main.tex
````

The compiled PDF will appear as `main.pdf`.

---

## 📑 Features

* Clean **problem/solution structure** using custom LaTeX environments.
* Highlighted **“To Submit”** sections via `tcolorbox`.
* **TikZ diagrams** for sets, probability, and geometry.
* Configurable **homework title page** with `\hwtitle{}` macro.
* Modular **styling** via `CEDT-Homework-style.sty`.
* Example **code snippets** in Python/Jupyter for computational problems.

---

## 👤 Author

* Name: *Patthadon Phengpinij (CEDT02)*
* Course: (2/2025) *2110573 Pattern Recognition* for CU CEDT (Elective Course)
---

📌 *This repo is mainly for educational purposes. Please do not copy directly; use it as reference for your own work.*
