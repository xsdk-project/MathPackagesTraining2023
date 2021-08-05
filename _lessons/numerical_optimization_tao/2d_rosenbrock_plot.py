# this import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import patheffects
from matplotlib.colors import LogNorm

# prep 3d plot area
fig = plt.figure()
ax = Axes3D(fig, azim=-125, elev=50)

# define 
size = 100
p1 = np.linspace(-2, 2., size)
p2 = np.linspace(-1, 3., size)
P1, P2 = np.meshgrid(p1, p2)
F = (1.-P1)**2 + 100.*(P2-P1*P1)**2

# plot Rosenbrock surface 
ax.plot_surface(P1, P2, F, rstride=1, cstride=1, norm=LogNorm(),
                linewidth=0, edgecolor='none', cmap="viridis", zorder=0)
# plot optimum solution at f(1, 1) = 0
ax.plot([1.], [1.], [0.], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5, zorder=5)

# set the axis limits
ax.set_xlim([-2, 2.0])
ax.set_ylim([-1, 3.0])
ax.set_zlim([0, 2500])

# set axis labels and save
ax.dist = 12
ax.set_xlabel(r'$p_1$')
ax.set_ylabel(r'$p_2$')
ax.set_zlabel(r'$f(p_1, p_2)$')
plt.savefig("2d_rosenbrock.png")
plt.close()

# 2D contour plot of base rosenbrock with enlarged boundaries
fig, ax = plt.subplots()
levels = [0.0, 0.1, 1.0, 10.0, 100.0, 1000.0]
p1 = np.linspace(-3, 3., size)
p2 = np.linspace(-2, 4., size)
P1, P2 = np.meshgrid(p1, p2)
F = (1.-P1)**2 + 100.*(P2-P1*P1)**2
ax.contour(P1, P2, F, levels, colors='black', linewidths=0.5)
plt.imshow(F, extent=[-3, 3, -2, 4], origin='lower', cmap='viridis', alpha=0.5)
plt.colorbar()
ax.plot([1.], [1.], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5, zorder=5)

plt.xlabel(r'$p_1$')
plt.ylabel(r'$p_2$')
plt.savefig("2d_rosenbrock_contour.png")
plt.close()

# contour plot with equality constraint
fig, ax = plt.subplots()
levels = [0.0, 0.1, 1.0, 10.0, 100.0, 1000.0]
p1 = np.linspace(-3, 3., size)
p2 = np.linspace(-2, 4., size)
P1, P2 = np.meshgrid(p1, p2)
F = (1.-P1)**2 + 100.*(P2-P1*P1)**2
ax.contour(P1, P2, F, levels, colors='black', linewidths=0.5)
plt.imshow(F, extent=[-3, 3, -2, 4], origin='lower', cmap='viridis', alpha=0.5)
plt.colorbar()

xx = p1
yy = -(xx - 1.0)**2.0 + 3
ax.plot(xx, yy, 'k--', alpha=0.5, linewidth=2, label=r'$(p_1 - 1)^2 + p_2 - 3 = 0$')
ax.plot([1.61773], [2.61842], markerfacecolor='r', markeredgecolor='k', markeredgewidth=0.5, marker='o', markersize=5)
ax.plot([-0.617224], [0.384585], markerfacecolor='r', markeredgecolor='k', markeredgewidth=0.5, marker='o', markersize=5)

ax.set_xlim([-3, 3.0])
ax.set_ylim([-2, 4.0])
plt.xlabel(r'$p_1$')
plt.ylabel(r'$p_2$')
plt.legend(loc='best')
plt.savefig("2d_rosenbrock_eq.png")
plt.close()

# contour plot with bounds
fig, ax = plt.subplots()
levels = [0.0, 0.1, 1.0, 10.0, 100.0, 1000.0]
p1 = np.linspace(-3, 3., size)
p2 = np.linspace(-2, 4., size)
P1, P2 = np.meshgrid(p1, p2)
F = (1.-P1)**2 + 100.*(P2-P1*P1)**2
ax.contour(P1, P2, F, levels, colors='black', linewidths=0.5)
plt.imshow(F, extent=[-3, 3, -2, 4], origin='lower', cmap='viridis', alpha=0.5)
plt.colorbar()

xx = np.linspace(0., -3., size)
ax.plot(xx, np.zeros(xx.shape), 'k', alpha=0.5, linewidth=2, path_effects=[patheffects.withTickedStroke(spacing=7)], label=r'$p_1 \leq 0$ and $p_2 \geq 0$')
yy = np.linspace(4., 0., size)
ax.plot(np.zeros(yy.shape), yy, 'k', alpha=0.5, linewidth=2, path_effects=[patheffects.withTickedStroke(spacing=7)])
ax.plot([0.], [0.], markerfacecolor='r', markeredgecolor='k', markeredgewidth=0.5, marker='o', markersize=5)

ax.set_xlim([-3, 3.0])
ax.set_ylim([-2, 4.0])
plt.xlabel(r'$p_1$')
plt.ylabel(r'$p_2$')
plt.legend(loc='best')
plt.savefig("2d_rosenbrock_bound.png")
plt.close()

# contour plot with all
fig, ax = plt.subplots()
levels = [0.0, 0.1, 1.0, 10.0, 100.0, 1000.0]
p1 = np.linspace(-3, 3., size)
p2 = np.linspace(-2, 4., size)
P1, P2 = np.meshgrid(p1, p2)
F = (1.-P1)**2 + 100.*(P2-P1*P1)**2
ax.contour(P1, P2, F, levels, colors='black', linewidths=0.5)
plt.imshow(F, extent=[-3, 3, -2, 4], origin='lower', cmap='viridis', alpha=0.5)
plt.colorbar()

xx = p1
yy = -(xx - 1.0)**2.0 + 3
ax.plot(xx, yy, 'k--', alpha=0.5, linewidth=2, label=r'$(p_1 - 1)^2 + p_2 - 3 = 0$')
ax.plot([-0.617224], [0.384585], markerfacecolor='r', markeredgecolor='k', markeredgewidth=0.5, marker='o', markersize=5)

xb = np.linspace(0., -3., size)
ax.plot(xb, np.zeros(xb.shape), 'k', alpha=0.5, linewidth=2, path_effects=[patheffects.withTickedStroke(spacing=7)], label=r'$p_1 \leq 0$ and $p_2 \geq 0$')
yb = np.linspace(4., 0., size)
ax.plot(np.zeros(yb.shape), yb, 'k', alpha=0.5, linewidth=2, path_effects=[patheffects.withTickedStroke(spacing=7)])

ax.set_xlim([-3, 3.0])
ax.set_ylim([-2, 4.0])
plt.xlabel(r'$p_1$')
plt.ylabel(r'$p_2$')
plt.legend(loc='best')
plt.savefig("2d_rosenbrock_bound_eq.png")
plt.close()