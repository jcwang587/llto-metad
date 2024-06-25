library(metadynminer3d)
library(rgl)

hillsf <- read.hills3d("HILLS_700K")

# Create the FES data
xl <- c(-0.5, 4.5)
yl <- c(-0.5, 4.5)
zl <- c(-0.5, 4.5)
tfes <- fes(hillsf, xlim=xl, ylim=yl, zlim=zl)
tfes <- tfes - min(tfes)

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

myColorKey.at <- seq(0, 0.4, 0.04)
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
svg("700K_XZ.svg", width=7, height=7)
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
svg("700K_XY.svg", width=7, height=7)
print(lp_xy)
dev.off()

r_yz <- raster(slice_x_2D)
lp_yz <- levelplot(r_yz, 
                   margin=FALSE, 
                   cuts=11, 
                   col.regions=colorRampPalette(brewer.pal(9, "YlOrRd")),
                   par.settings = myTheme,
                   at = myColorKey.at,
                   colorkey = myColorKey.ckey,
                   panel = custom_panel
)

# Export the plot in YZ plane in png format
svg("700K_YZ.svg", width=7, height=7)
print(lp_yz)
dev.off()


library(ggplot2)

# Define constants
kb <- 8.617333262145e-5 # Boltzmann constant in eV/K
T <- 700
beta <- 1 / (kb * T) # Inverse temperature in 1/(Joules)

# Define the grid spacing
dx <- (xmax - xmin) / (length(unique(tfes$x)) - 1)
dy <- (ymax - ymin) / (length(unique(tfes$y)) - 1)

# Initialize an empty vector for F(z)
F_z = numeric(length(unique(tfes$z)))

# Calculate F(z) by looping over each z index
for (z_idx in 1:length(unique(tfes$z))) {
  z_value <- unique(tfes$z)[z_idx]
  sum_exp_F <- 0
  
  for (x_idx in 1:(length(unique(tfes$x)) - 1)) {
    for (y_idx in 1:(length(unique(tfes$y)) - 1)) {
      # Calculate the Boltzmann factor for the 4 grid points around (x_i, y_j)
      exp_F_i_j = exp(-beta * tfes$fes[x_idx, y_idx, z_idx])
      exp_F_i1_j = exp(-beta * tfes$fes[x_idx + 1, y_idx, z_idx])
      exp_F_i_j1 = exp(-beta * tfes$fes[x_idx, y_idx + 1, z_idx])
      exp_F_i1_j1 = exp(-beta * tfes$fes[x_idx + 1, y_idx + 1, z_idx])
      
      # Use the trapezoidal rule to approximate the integral at the current grid point
      sum_exp_F <- sum_exp_F + (exp_F_i_j + exp_F_i1_j + exp_F_i_j1 + exp_F_i1_j1) / 4
    }
  }
  
  # Multiply by the area element and take the negative logarithm to calculate F(z)
  F_z[z_idx] <- -kb * T * log(dx * dy * sum_exp_F)
}

F_z <- F_z - min(F_z)
data <- data.frame(x=unique(tfes$z)/4, y=F_z)

# Generate the plot with specified axis label intervals
p <- ggplot(data, aes(x=x, y=y)) +
  geom_smooth(span=0.3, method='loess', formula=y ~ x, color='#193E8F', fill='#55B7E6', linewidth=1.5) +
  scale_x_continuous(breaks=seq(floor(min(data$x)), ceiling(max(data$x)), by=0.2)) + 
  xlab("Relative Coordinate (Z)") +
  ylab("Free Energy (eV)") +
  theme(axis.text=element_text(size=18),
        axis.title=element_text(size=20))

# Save the plot with the specified dimensions

ggsave("700K_projected_z.png", plot=p, width=10, height=6)

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


