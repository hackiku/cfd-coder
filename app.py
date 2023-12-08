import streamlit as st

# This is your main app file for the Streamlit multipage app.
# Streamlit will automatically add navigation to the sidebar for each page in the 'pages' folder.

def main():
    st.title('CFD dynamite 🛰️')

    # Any general instructions or app-wide information can go here.
    
    st.latex("""
    \begin{align*}
    -2x^2t\frac{\partial y}{\partial x}+\frac{\partial u}{\partial t}&=4 \\
    4a^2B\cdot4(x,0)&=x^2 \\
    a&=-2x^2t=\frac{\partial x}{\partial r} \\
    b&=1=\frac{\partial z}{\partial t} \\
    c&=u=\frac{\partial u}{\partial r} \\
    v-2x^2\sigma r&=0 \\
    \frac{\partial x}{x^2}&=-2\sigma\partial\Gamma \\
    -\frac{1}{x}&=-2\frac{r^2}{x}+s \\
    -x&=-r^2+5 \\
    r&=t \\
    s&=x-\frac{1}{\Gamma^2} \\
    x&=\frac{1}{r^2}+5 \\
    \frac{1}{x}&=r^2+5 \\
    1&=x(r+5) \\
    t&=\Gamma \\
    x&=\frac{1}{r^2}+5 \\
    \frac{\partial u}{u}&=\partial r \\
    u&=e^{r}\cdot e(s)=e^r\cdot s \\
    u(x,0)&=x^2=(\frac{1}{c^2}+5)^2 \\
    u(0,s)&=s \\
    u(r,s)&=e^r\cdot s \\
    u(x,t)&=(\epsilon^{+}\cdot(x-\frac{1}{t^2}))^{2}
    \end{align*}
    """)

if __name__ == "__main__":
    main()

with st.sidebar:
    st.header('Slajdovi objasnjeni sa AI')
    st.info('Klikci meni za predmete')
