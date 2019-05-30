from PIL import Image, ImageDraw

def carre(x0, y0):
  LT = (x0, y0)
  LB = (x0, y0+dy)
  RT = (x0+dx, y0)
  RB = (x0+dx, y0+dy)
  gris = (220, 220, 220)
  grisfonce = (100, 100, 100)
  red = (255, 200, 200)
  d.line([LT, RT, RB, LB, LT], fill=gris, width=1)

print ("Dessin de la grid carré")
width = 2700
height = 2100
dx=20
dy=dx
Nx=int(width/dx)
Ny=int(height/dy)
im = Image.new('RGB', (width, height), color = 'white')
d = ImageDraw.Draw(im)
for i in range(0, Nx):  
  for j in range(0, Ny):  
    carre(i*dx, j*dy)
im.save("grid_carre.png")
