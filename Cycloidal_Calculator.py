import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def cycloidal_disk_shape(R, Rr, e, N, num_points):
    """
    Calculates x and y coordinates for the cycloidal disk shape.

    Args:
        R (float): Rolling circle radius (mm).
        Rr (float): Roller radius (mm).
        E (float): Eccentricity (mm).
        N (int): Number of rollers.
        num_points (int): Number of points to calculate.

    Returns:
        tuple: Tuple containing x and y coordinates (numpy arrays).
    """

    t = np.linspace(0.0, 2*np.pi, num_points)

    # Calculate x and y coordinates
    x = (R * np.cos(t)) - (Rr * np.cos(t + np.arctan(np.sin((1-N) * t) / ((R / (e * N)) - np.cos((1-N) * t))))) - (e * np.cos(N * t))
    y = (-R * np.sin(t)) + (Rr * np.sin(t + np.arctan(np.sin((1-N) * t) / ((R / (e * N)) - np.cos((1-N) * t))))) + (e * np.sin(N * t))

    return x, y

def main():
    st.set_page_config(page_title="Cycloidal Disk Shape Plotter", page_icon=":gear:")
    st.title("Cycloidal Disk Shape Plotter")
    st.markdown("Designed and created by Donald Le [<img src='https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg' alt='LinkedIn' width='30' height='30'/>](https://www.linkedin.com/in/donald-le/) \
        [<img src='https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/112-gmail_email_mail-1024.png' alt='mail.png' width='30' height='30'/>](mailto:donaldle@berkeley.edu) \
        [<img src='https://p7.hiclipart.com/preview/1023/278/478/computer-icons-symbol-clip-art-website-logo-thumbnail.jpg' alt='website' width='25' height='25'/>](https://www.donaldle.com)", unsafe_allow_html=True)
    
  
    st.image('Cycloidal_Diagram.png')
    # Input parameters with sliders
    D = st.slider("Outer diameter (Path Circle Diameter) (D) (mm)", min_value=10.0, value=100.0, step=0.5, max_value=250.0)
    dp = st.slider("Diameter of pins (dp) (mm)", min_value=1.0, step=0.1,value=4.0, max_value=20.0)
    N = st.slider("Number of pins (N)", min_value=2, step=1, value=26, max_value=150)
    e = st.slider("Eccentricity (e) (mm)", min_value=0.05, step=0.01,value=0.5, max_value=float((np.floor(((D/N)/2.0)*10)/10)))


    Rr = dp / 2
    R = (D) / 2
    num_points = 10000
    
   

    # Calculate disk and bearing centers
    center_x = 0 
    center_y = 0  

    # Calculate shape
    x, y = cycloidal_disk_shape(R, Rr, e, N, num_points)

    # Create Matplotlib plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(x, y, label="Cycloidal Disk")

    # Plot outer pins
    pin_angles = np.linspace(0, 2*np.pi, N, endpoint=False)  # Exclude the last angle to have N-1 pins
    pin_x = center_x + (R) * np.cos(pin_angles)
    pin_y = center_y + (R) * np.sin(pin_angles)
    
    fig.canvas.draw()
    size = fig.get_size_inches()
    
    for i in range(N):
        ax.add_patch(plt.Circle((pin_x[i], pin_y[i]), dp/2,color='red'))
    
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.set_title("Cycloidal Disk Shape with Outer Pins")
    ax.axis('equal')
    ax.grid(True)
    ax.margins(0.1, 0.1)
    # Display plot
    
    st.pyplot(fig)
    st.title("Outputs")
    st.subheader("Gear Reduction")
    st.write("Gear Reduction ->",str(int(N-1)),": 1")
    st.subheader("Disk Hole Diameter")
    drp = st.slider("Diameter of drive pins (mm)", min_value=1.0, step=0.1, value=D/3)
    st.write("Disk Hole Diameter(mm):",str(round((drp+2*e)*1000)/1000))
    
    
    st.subheader("Generated Cycloidal Disk Equations:")
    st.write("x = (",str(int(R)),"*cos(t))-(",str(Rr),"*cos(t+arctan(sin((1-",str(int(N)),")*t)/((",str(int(R)),"/(",str(e),"*",str(int(N)),"))-cos((1-",str(int(N)),")*t)))))-(",str(e),"*cos(",str(int(N)),"*t))")
    st.write("y = (",str(int(-R)),"*sin(t))+(",str(Rr),"*sin(t+arctan(sin((1-",str(int(N)),")*t)/((",str(int(R)),"/(",str(e),"*",str(int(N)),"))-cos((1-",str(int(N)),")*t)))))+(",str(e),"*sin(",str(int(N)),"*t))")
    
    
    st.header("Sources:")
    st.write("[[1]](https://howtomechatronics.com/how-it-works/harmonic-vs-cycloidal-drive-designing-3d-printing-testing/)[[2]](https://www.tec-science.com/mechanical-power-transmission/planetary-gear/construction-of-the-cycloidal-disc/)[[3]](https://blogs.solidworks.com/teacher/wp-content/uploads/sites/3/Building-a-Cycloidal-Drive-with-SOLIDWORKS.pdf)[[4]](https://en.wikipedia.org/wiki/Cycloidal_drive)")

             
             
if __name__ == "__main__":
    main()
