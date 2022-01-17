#The point sets sometimes are stored in .hdf files (that can be read by h5py easily), sometimes the files are .off. 
#This function reads an .off file into a 2d Nx3 list (each row is corresponding to a point coordinates) 
def off_to_2d_list(f):
  f.readline()#to get rid of the first line which is the term OFF
  no_vertices = int(f.readline().split(" ")[0])
  x = [];  y = []; z = []
  for i in range(0,no_vertices):
    xx,yy,zz = f.readline().split(" ")
    x.append(float(xx))
    y.append(float(yy))
    z.append(float(zz))
  f.close()
  return [x,y,z]
