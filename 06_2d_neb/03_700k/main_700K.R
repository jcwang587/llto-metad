library(metadynminer3d)
library(rgl)

hillsf <- read.hills3d("HILLS_700K")

# Create the FES data
xl <- c(-0.5, 4.5)
yl <- c(-0.5, 4.5)
zl <- c(-0.5, 4.5)
tfes <- fes(hillsf, xlim=xl, ylim=yl, zlim=zl)
tfes <- tfes - min(tfes)
minima <- fesminima(tfes)

# Determine the middle y index
mid_y_index <- ceiling(length(unique(tfes$y)) / 2)

# Extract the 2D slice at the middle y-plane from the 3D array tfes$fes
slice_y_2D <- tfes$fes[,mid_y_index,]

library(reticulate)
y_fes_700k <- array(slice_y_2D, dim = c(64, 64))
np_save <- import("numpy")$save
np_save("y_fes_700k.npy", y_fes_700k)




