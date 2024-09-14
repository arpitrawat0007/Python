from sketchpy import canvas
from sklearn.preprocessing import scale
pen = canvas.sketch_from_svg("C:\\Users\\arpit\\OneDrive\\Pictures\\Saved Pictures\\Image.svg",scale = 250)

pen.draw()