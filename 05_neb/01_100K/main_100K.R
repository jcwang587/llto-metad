library(ggplot2)
library(metadynminer)

hillsf <- read.hills("HILLS_100K_2D")

# Create the FES data
xl <- c(-0.5, 4.5)
yl <- c(-0.5, 4.5)
zl <- c(-0.5, 4.5)
tfes_2d <- fes(hillsf, xlim=xl, zlim=zl)
tfes_2d <- tfes_2d - min(tfes_2d)
minima_2d <- fesminima(tfes_2d)
myneb_bc <-neb(minima_2d, min1="B", min2="C", nstep=10000)
myneb_ca <-neb(minima_2d, min1="C", min2="A", nstep=10000)
myneb_ad <-neb(minima_2d, min1="A", min2="D", nstep=10000)
myneb_db <-neb(minima_2d, min1="D", min2="B", nstep=10000)

png("neb_100k.png")
plot(minima_2d)
linesonfes(myneb_bc)
linesonfes(myneb_ca)
linesonfes(myneb_ad)
linesonfes(myneb_db) 
dev.off()

library(reticulate)
bc_fespot <- array(myneb_bc$path$fespot, dim = c(21))
ca_fespot <- array(myneb_ca$path$fespot, dim = c(21))
ad_fespot <- array(myneb_ad$path$fespot, dim = c(21))
db_fespot <- array(myneb_db$path$fespot, dim = c(21))

np_save <- import("numpy")$save
np_save("bc_fespot_100k.npy", bc_fespot)
np_save("ca_fespot_100k.npy", ca_fespot)
np_save("ad_fespot_100k.npy", ad_fespot)
np_save("db_fespot_100k.npy", db_fespot)




