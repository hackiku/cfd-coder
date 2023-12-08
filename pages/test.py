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

  # ====================================

  st.header("1. Determine the type of PDE")

  st.markdown("""
  To classify a second-order linear PDE, we look at the discriminant of the quadratic form of the PDE, which is given by $$D = B^2 - 4AC$$. The coefficients $$A$$, $$B$$, and $$C$$ come from the standard form of the PDE $$Au_{xx} + 2Bu_{xy} + Cu_{yy}$$. Here's the analysis for the given PDE:
  """, unsafe_allow_html=True)

  st.latex(r"""
  \begin{align*}
  &\text{Given PDE: } u_{xx} + 2u_{xy} - 5u_{yy} - 7u = 3x \\
  &\text{Comparing with standard form: } Au_{xx} + 2Bu_{xy} + Cu_{yy} = D(x, y), \text{ we get:} \\
  &A = 1, \quad B = 1, \quad C = -5 \\
  &\text{Discriminant is: } D = B^2 - 4AC = 1^2 - 4 \cdot 1 \cdot (-5) = 1 + 20 = 21 > 0
  \end{align*}
  """)

  st.markdown("""
  Since the discriminant $$D$$ is positive, the PDE is hyperbolic. Hyperbolic PDEs often describe wave phenomena and propagation, where solutions may have characteristics that are real and distinct.
  """, unsafe_allow_html=True)

  spacer("2em")

  st.markdown("""
  Next, let's analyze the regions where the PDE $$\sqrt{u} u_{xx} - 2u_{xy} + e^u u_{yy} + u = 4$$ is parabolic, elliptic, or hyperbolic:
  """, unsafe_allow_html=True)

  st.latex(r"""
  \begin{align*}
  &\text{For the given PDE: } \sqrt{u} u_{xx} - 2u_{xy} + e^u u_{yy} + u = 4, \text{ we have:} \\
  &A = \sqrt{u}, \quad B = -1, \quad C = e^u \\
  &\text{Discriminant is: } D = B^2 - 4AC = (-1)^2 - 4 \cdot (\sqrt{u}) \cdot (e^u) = 1 - 4 \cdot u^{0.5} \cdot e^u
  \end{align*}
  """)

  st.markdown("""
  The discriminant $$D$$ varies depending on the value of $$u$$:
  - For $$u > 0$$, $$D$$ can be either positive or negative, depending on the magnitude of $$u$$.
  - For $$u = 0$$, $$D = 1$$, which makes the PDE parabolic.
  - For $$u < 0$$, $$D$$ is always positive, indicating a hyperbolic PDE.

  In different regions of the domain, the nature of the PDE changes, which affects the approach to finding solutions.
  """, unsafe_allow_html=True)

  spacer("2em")

  # ===================

  st.header("3. Determine the solution of the PDE")

  st.markdown("""
  Given the partial differential equation (PDE):

  $$ u_t - 2x^2 \\frac{\\partial^2 u}{\\partial x^2} = 0, $$

  for $$ -\\infty < x < \\infty, $$ and $$ t > 0, $$ with the initial condition $$ u(x,0) = x^2, $$ we aim to find the solution $$ u(x,t) $$. This type of PDE can be approached by the method of characteristics, where we look for curves along which the PDE becomes an ordinary differential equation (ODE).

  Firstly, we identify the characteristic equations from the PDE:

  $$ \\frac{dx}{dt} = -2x^2 $$

  $$ \\frac{du}{dt} = 0 $$

  Integrating the first characteristic equation with respect to $$ t $$, we find:

  $$ -\\frac{1}{x} = -2t + \\frac{1}{x_0}, $$

  where $$ x_0 $$ is the value of $$ x $$ when $$ t=0 $$. This can be rearranged to give the characteristic curves:

  $$ x(t) = \\frac{1}{2t + \\frac{1}{x_0}} $$

  Since $$ \\frac{du}{dt} = 0 $$, the solution $$ u $$ is constant along these characteristic curves. Therefore, the solution can be expressed using the initial condition $$ u(x,0) = x^2 $$:

  $$ u(x,t) = u\\left(\\frac{1}{2t + \\frac{1}{x_0}}, 0\\right) = \\left(\\frac{1}{2t + \\frac{1}{x_0}}\\right)^2 $$

  Solving for $$ x_0 $$ in terms of $$ x $$ and $$ t $$ from the characteristic equation, we obtain:

  $$ x_0 = \\frac{1}{\\frac{1}{x} + 2t} $$

  Substituting $$ x_0 $$ back into the solution for $$ u $$, we get:

  $$ u(x,t) = \\left(\\frac{1}{2t + \\frac{1}{x}}\\right)^2 $$

  Or simplified,

  $$ u(x,t) = \\left(\\frac{x}{1 + 2xt}\\right)^2 $$

  This represents the solution to our initial-value problem.
  """, unsafe_allow_html=True)

  spacer("2em")


if __name__ == "__main__":
    main()
