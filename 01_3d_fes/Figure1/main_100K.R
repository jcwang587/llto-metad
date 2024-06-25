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
library(latticeExtra)

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
  panel.abline(h = 0.1, col = "black", lwd = 20, lty = 2)
  panel.abline(v = 0.1, col = "black", lwd = 20, lty = 2)
  panel.abline(h = 0.9, col = "black", lwd = 20, lty = 2)
  panel.abline(v = 0.9, col = "black", lwd = 20, lty = 2)
}

r_xz <- raster(slice_y_2D)

# Define the level plot
lp_xz <- levelplot(r_xz, 
                   margin=FALSE, 
                   cuts=11, 
                   col.regions=colorRampPalette(brewer.pal(9, "YlOrRd")),
                   par.settings = myTheme,
                   at = seq(0, 0.45, 0.05),
                   colorkey = NULL,  # Hide the color key
                   xlab = NULL,  # Hide x-axis label
                   ylab = NULL,  # Hide y-axis label
                   scales = list(draw = FALSE),  # Hide axis ticks
                   panel = custom_panel
)

# Export the plot in XZ plane in png format
jpeg("FES_XZ_100K.png", width=3200, height=3200)
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
                   at = seq(0, 0.45, 0.05),
                   colorkey = NULL,  # Hide the color key
                   xlab = NULL,  # Hide x-axis label
                   ylab = NULL,  # Hide y-axis label
                   scales = list(draw = FALSE),  # Hide axis ticks
                   panel = custom_panel
)

# Export the plot in XY plane
jpeg("FES_XY_100K.png", width=3200, height=3200)
print(lp_xy)
dev.off()


r_yz <- raster(slice_x_2D)
lp_yz <- levelplot(r_yz, 
                   margin=FALSE, 
                   cuts=11, 
                   col.regions=colorRampPalette(brewer.pal(9, "YlOrRd")),
                   par.settings = myTheme,
                   at = seq(0, 0.45, 0.05),
                   colorkey = NULL,  # Hide the color key
                   xlab = NULL,  # Hide x-axis label
                   ylab = NULL,  # Hide y-axis label
                   scales = list(draw = FALSE),  # Hide axis ticks
                   panel = custom_panel
)

# Export the plot in YZ plane in png format
jpeg("FES_YZ_100K.png", width=3200, height=3200)
print(lp_yz)
dev.off()

