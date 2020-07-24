from geometryDiffVisualization import *

g1 = MuonGeometry("BarrelPG2009.xml")
g2 = MuonGeometry("BarrelReco_0T.xml")
draw_station(g1, g2, 1, "barrel0Ttest_100x_station1.svg", length_factor=100., angle_factor=100., dropafew=True)
draw_station(g1, g2, 2, "barrel0Ttest_100x_station2.svg", length_factor=100., angle_factor=100., dropafew=True)
draw_station(g1, g2, 3, "barrel0Ttest_100x_station3.svg", length_factor=100., angle_factor=100., dropafew=True)
draw_station(g1, g2, 4, "barrel0Ttest_100x_station4.svg", length_factor=100., angle_factor=100., dropafew=True)
draw_wheel(g1, g2, -2, "barrel0Ttest_100x_wheelm2.svg", length_factor=100., angle_factor=100., dropafew=True)
draw_wheel(g1, g2, -1, "barrel0Ttest_100x_wheelm1.svg", length_factor=100., angle_factor=100., dropafew=True)
draw_wheel(g1, g2,  0, "barrel0Ttest_100x_wheelze.svg", length_factor=100., angle_factor=100., dropafew=True)
draw_wheel(g1, g2, +1, "barrel0Ttest_100x_wheelp1.svg", length_factor=100., angle_factor=100., dropafew=True)
draw_wheel(g1, g2, +2, "barrel0Ttest_100x_wheelp2.svg", length_factor=100., angle_factor=100., dropafew=True)

