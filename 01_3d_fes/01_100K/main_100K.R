library(metadynminer3d)
library(rgl)

hillsf <- read.hills3d("HILLS_100K")

# Create the FES data
xl <- c(-0.5, 4.5)
yl <- c(-0.5, 4.5)
zl <- c(-0.5, 4.5)
tfes <- fes(hillsf, xlim=xl, ylim=yl, zlim=zl)
tfes <- tfes - min(tfes)
minima <- fesminima(tfes)

# Determine the middle y index
mid_y_index <- ceiling(length(unique(tfes$y)) / 2)
mid_z_index <- ceiling(length(unique(tfes$z)) / 2)
mid_x_index <- ceiling(length(unique(tfes$x)) / 2)

# Extract the 2D slice at the middle y-plane from the 3D array tfes$fes
slice_y_2D <- tfes$fes[,mid_y_index,]
slice_z_2D <- tfes$fes[,,mid_z_index]
slice_x_2D <- tfes$fes[mid_x_index,,]

# Generate a 2D plot for the slice
library(raster)
library(rasterVis)
library(lattice)
library(RColorBrewer)
library(gridSVG)
library(latticeExtra)
library(lattice)

# Define a custom theme
myTheme <- list(
  axis.text=list(
    cex=2,  # Set font size for axis text
    fontfamily="Tahoma"
  )
)

myColorKey.at <- seq(0, 0.45, 0.05)
myColorKey.ckey <- list(at=myColorKey.at, labels=list(at=c(0, 0.1, 0.2, 0.3, 0.4)))

xmin <- min(tfes$x)
xmax <- max(tfes$x)
ymin <- min(tfes$y)
ymax <- max(tfes$y)
zmin <- min(tfes$z)
zmax <- max(tfes$z)

# Custom panel function to add lines
custom_panel <- function(x, y, ...) {
  panel.levelplot(x, y, ...)
  panel.abline(h = 0.1, col = "black", lwd = 2, lty = 2)
  panel.abline(v = 0.1, col = "black", lwd = 2, lty = 2)
  panel.abline(h = 0.9, col = "black", lwd = 2, lty = 2)
  panel.abline(v = 0.9, col = "black", lwd = 2, lty = 2)
}

r_xz <- raster(slice_y_2D)

lp_xz <- levelplot(r_xz, 
                   margin=FALSE, 
                   cuts=11, 
                   col.regions=colorRampPalette(brewer.pal(9, "YlOrRd")),
                   par.settings = myTheme,
                   at = myColorKey.at,
                   colorkey = myColorKey.ckey,
                   panel = custom_panel
)

# Export the plot in XZ plane
svg("100K_XZ.svg", width=7, height=7)
print(lp_xz)
dev.off()


# mirror the slice_z_2D based on the middle x index
slice_z_2D <- slice_z_2D[nrow(slice_z_2D):1,]

r_xy <- raster(slice_z_2D)
# switch x and y
r_xy <- t(r_xy)
lp_xy <- levelplot(r_xy, 
                   margin=FALSE, 
                   cuts=11, 
                   col.regions=colorRampPalette(brewer.pal(9, "YlOrRd")),
                   par.settings = myTheme,
                   at = myColorKey.at,
                   colorkey = myColorKey.ckey,
                   panel = custom_panel
)

# Export the plot in XY plane
svg("100K_XY.svg", width=7, height=7)
print(lp_xy)
dev.off()


r_yz <- raster(slice_x_2D)
lp_yz <- levelplot(r_yz, 
                   margin=FALSE, 
                   cuts=11, 
                   # xlab="Y coordinate",
                   # ylab="Z coordinate", 
                   # main="Central YZ Slice of FES @ 100 K",
                   col.regions=colorRampPalette(brewer.pal(9, "YlOrRd")),
                   par.settings = myTheme,
                   at = myColorKey.at,
                   colorkey = myColorKey.ckey,
                   panel = custom_panel
)

# Export the plot in YZ plane in png format
svg("100K_YZ.svg", width=7, height=7)
print(lp_yz)
dev.off()


# library(reticulate)
# fes_data_3d <- array(tfes$fes, dim = c(64, 64, 64))
# x_data_1d <- array(tfes$x, dim = c(64))
# y_data_1d <- array(tfes$y, dim = c(64))
# z_data_1d <- array(tfes$z, dim = c(64))
# # Use the NumPy save function to write the array to a .npy file
# np_save <- import("numpy")$save
# np_save("fes_data_3d.npy", fes_data_3d)
# np_save("x_data_1d.npy", x_data_1d)
# np_save("y_data_1d.npy", y_data_1d)
# np_save("z_data_1d.npy", z_data_1d)



# library(ggplot2)
# 
# hillsf <- read.hills("HILLS_100K_2D")
# 
# # Create the FES data
# tfes_2d <- fes(hillsf, xlim=xl, zlim=zl)
# tfes_2d <- tfes_2d - min(tfes_2d)
# minima_2d <- fesminima(tfes_2d)
# myneb_bc <-neb(minima_2d, min1="B", min2="C", nstep=10000)
# myneb_ca <-neb(minima_2d, min1="C", min2="A", nstep=10000)
# myneb_ad <-neb(minima_2d, min1="A", min2="D", nstep=10000)
# myneb_db <-neb(minima_2d, min1="D", min2="B", nstep=10000)
# 
# # plot neb
# plot(minima_2d)
# linesonfes(myneb_bc)
# linesonfes(myneb_ca)
# linesonfes(myneb_ad)
# linesonfes(myneb_db) 

library(reticulate)
fes_data_3d <- array(tfes$fes, dim = c(64, 64, 64))
x_data_1d <- array(tfes$x, dim = c(64))
y_data_1d <- array(tfes$y, dim = c(64))
z_data_1d <- array(tfes$z, dim = c(64))
# Use the NumPy save function to write the array to a .npy file
np_save <- import("numpy")$save
np_save("fes_data_3d.npy", fes_data_3d)
np_save("x_data_1d.npy", x_data_1d)
np_save("y_data_1d.npy", y_data_1d)
np_save("z_data_1d.npy", z_data_1d)



