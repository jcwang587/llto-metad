library(ggplot2)
library(metadynminer)

hillsf <- read.hills("HILLS_300K_2D")

# Create the FES data
xl <- c(-0.5, 4.5)
yl <- c(-0.5, 4.5)
zl <- c(-0.5, 4.5)
tfes_2d <- fes(hillsf, xlim=xl, zlim=zl)
tfes_2d <- tfes_2d - min(tfes_2d)
minima_2d <- fesminima(tfes_2d, nbin=36)

# myneb_bc <-neb(minima_2d, min1="A", min2="B", nstep=10000)
# 
png("neb_100k.png")
plot(minima_2d)
#linesonfes(myneb_bc)
dev.off()





