# Newton Fractals & Numerical Methods
A mathematical exploration of root-finding algorithms, polynomial interpolation,
and complex dynamics — culminating in the generation of Newton Fractals.
Built as a research project during Year 1.
## What is a Newton Fractal?

Newton's method is an iterative algorithm for finding roots of a function.
When applied to polynomials in the **complex plane**, each point either:
- Converges to one of the polynomial's roots, or
- Diverges / oscillates at the boundary

Coloring each point by **which root it converges to** and **how fast**
produces a stunning fractal — the Newton Fractal.

The boundaries between regions of convergence are infinitely complex,
and this is where chaos lives.

---

## Project Structure
newton-fractals/
    ├── src/
    │   ├── complex_class.py      # Complex number class with full operator overloading
    │   ├── root_finding.py       # Bisection, Newton-Raphson, Secant, Regula Falsi
    │   ├── interpolation.py      # Lagrange, Hermite, Cubic Hermite interpolation
    │   └── fractal.py            # Newton Fractal generator
    │
    ├── visualizations/
    │   ├── newton_fractal.png    # Static fractal image
    │   ├── fractal_zoom.gif      # Animated zoom into fractal boundary
    │   └── convergence.png       # Convergence rate comparison across methods
    │
    ├── exposition/
    │   └── report.pdf            # Full mathematical write-up
    │
    ├── requirements.txt
    └── README.md
