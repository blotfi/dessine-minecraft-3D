from PIL import Image, ImageDraw

def losange(x0, y0):
  left = (x0, y0)
  top = (x0+dx, y0-dy)
  right = (x0+2*dx, y0)
  bottom = (x0+dx, y0+dy)
  gris = (220, 220, 220)
  red = (255, 200, 200)
  d.line([left, top, right, bottom, left], fill=gris, width=1)
  d.line([top, bottom], fill=red, width=1)
  d.line([(x0, y0-dy), (x0, y0+dy)], fill=red, width=1)

print ("Dessin de la grid iso")
width = 2700
height = 2100
dx=50
r3_2=0.86602540378444
l=dx/r3_2
dy=l*0.5
Nx=int(width/2/dx)
Ny=int(height/2/dy)
im = Image.new('RGB', (width, height), color = 'white')
d = ImageDraw.Draw(im)
for i in range(0, Nx):  
  for j in range(0, Ny):  
    losange(i*dx*2, j*dy*2)
im.save("grid_iso.png")
