import streamlit as st

def spacer(height='5em'):
  spacer_html = f'<div style="margin: {height};"></div>'
  st.markdown(spacer_html, unsafe_allow_html=True)

def main():
  st.title('Test prep')

  # Point 1
  st.write("1. Determine the type of PDE:")
  st.latex("u_{xx} + 2u_{xy} - 5u_{yy} - 7u = 3x")

  # Point 2
  st.write("2. Determine the regions where the PDE is parabolic, elliptic, or hyperbolic:")
  st.latex("\\sqrt{u} u_{xx} - 2u_{xy} + e^u u_{yy} + u = 4")

  # Point 3
  st.write("3. Determine the solution of the PDE:")
  st.latex("u_t - 2x^2 \\frac{\\partial^2 u}{\\partial x^2} = 0, \\text{ for } -\\infty < x < \\infty, t > 0, \\text{ with the initial condition } u(x,0) = x^2.")

  # Point 4
  st.write("4. Sketch the characteristics and solve the PDE:")
  st.latex("-e^u \\frac{\\partial u}{\\partial x} = \\frac{\\partial u}{\\partial t}, \\text{ with the initial conditions:}")
  st.latex("""
  u(x,0) = 
  \\begin{cases} 
  1, & x \\leq -2 \\\\
  0, & x > -2
  \\end{cases}
  """)

  # Point 5
  st.write("5. Sketch the characteristics and solve the PDE:")
  st.latex("\\sin(u) \\frac{\\partial u}{\\partial x} = \\frac{\\partial u}{\\partial t}, \\text{ with the initial conditions:}")
  st.latex("""
  u(x,0) = 
  \\begin{cases} 
  -\\frac{\\pi}{2}, & x < 1 \\\\
  0, & x > 1
  \\end{cases}
  """)

  st.markdown("***")

  # ============
  
  st.header("1. Determine the type of PDE")

  st.write("""
  To classify a second-order linear PDE, we look at the discriminant of the quadratic form of the PDE, which is given by \( D = B^2 - 4AC \). The coefficients \( A \), \( B \), and \( C \) come from the standard form of the PDE \( Au_{xx} + 2Bu_{xy} + Cu_{yy} \). Here's the analysis for the given PDE:
  """)

  st.latex(r"""
  \begin{align*}
  &\text{Given PDE: } u_{xx} + 2u_{xy} - 5u_{yy} - 7u = 3x \\
  &\text{Comparing with standard form: } Au_{xx} + 2Bu_{xy} + Cu_{yy} = D(x, y), \text{ we get:} \\
  &A = 1 \\
  &B = 2 \\
  &C = -5 \\
  &\text{Discriminant is: } D = B^2 - 4AC = 2^2 - 4(1)(-5) = 4 + 20 = 24 > 0
  \end{align*}
  """)

  st.write("""
  Since the discriminant \( D \) is positive, the PDE is hyperbolic. Hyperbolic PDEs often describe wave phenomena and propagation, where solutions may have characteristics that are real and distinct.
  """)

  spacer("2em")

  st.write("""
  Now let's analyze the regions where the PDE \( \sqrt{u} u_{xx} - 2u_{xy} + e^u u_{yy} + u = 4 \) is parabolic, elliptic, or hyperbolic:
  """)

  st.latex(r"""
  \begin{align*}
  &\text{For the given PDE: } \sqrt{u} u_{xx} - 2u_{xy} + e^u u_{yy} + u = 4, \text{ we have:} \\
  &A = \sqrt{u} \\
  &B = -1 \\
  &C = e^u \\
  &\text{Discriminant is: } D = B^2 - 4AC = (-1)^2 - 4(\sqrt{u})(e^u) = 1 - 4u^{0.5}e^u
  \end{align*}
  """)

  st.write("""
  The type of PDE changes based on the sign of the discriminant:
  - If \( D > 0 \), the PDE is hyperbolic.
  - If \( D = 0 \), the PDE is parabolic.
  - If \( D < 0 \), the PDE is elliptic.

  For different values of \( u \), we can determine the nature of the PDE in those regions.
  """)

  spacer("2em")

if __name__ == "__main__":
    main()
