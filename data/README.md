# Data preparation before using scripts transferring COLMAP results
## About the data structure 
The data structure should look like tat_root-->(dense, ...)-->(images, sparse, stereo, delaunay_photometric.ply, ...). The original structure directly out of COLMAP looks like tat_root-->(dense, ...)-->0-->(images, sparse, stereo, delaunay_photometric.ply, ...), you need to delete that "0" layer.
## About the point cloud file
The meshing method in dense reconstruction should be delaunay insead of possion; The original name from COLMAP of this point cloud is "meshed-delaunay.ply", you need to change it to "delaunay_photometric.ply". 