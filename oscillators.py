import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


def unit_circle() -> None:
  max = 2*np.pi
  step = max/99
  t_range = np.arange(0, max + step, step)

  f_t = lambda t: np.e ** (t * 1j)

  plt.plot(f_t(t_range).real, f_t(t_range).imag)

  plt.plot([0, f_t(0).real], [0, f_t(0).imag])

  plt.plot([0, f_t(np.pi/6).real], [0, f_t(np.pi/6).imag])

  plt.plot([0, f_t(np.pi/4).real], [0, f_t(np.pi/4).imag])

  plt.plot([0, f_t(np.pi/3).real], [0, f_t(np.pi/3).imag])

  plt.plot([0, f_t(np.pi/2).real], [0, f_t(np.pi/2).imag])

  plt.text(f_t(0).real, f_t(0).imag, "$0$")
  plt.text(f_t(np.pi/6).real, f_t(np.pi/6).imag, "$\pi/6$")
  plt.text(f_t(np.pi/4).real, f_t(np.pi/4).imag, "$\pi/4$")
  plt.text(f_t(np.pi/3).real, f_t(np.pi/3).imag, "$\pi/3$")
  plt.text(f_t(np.pi/2).real, f_t(np.pi/2).imag, "$\pi/2$")

  plt.legend(["$e^{it}$"], loc="upper right")
  plt.xlabel("Real")
  plt.ylabel("Imaginary")
  plt.title("Unit Circle")

  plt.show()

  return


def oscillator_threeD_plot() -> None:
  max = 8 * np.pi
  step = max / 99
  t_range = np.arange(0, max + step, step)

  f_t = lambda t: np.e ** (t * 1j)
  fig = plt.figure()
  ax1 = fig.add_subplot(projection='3d')
  ax1.plot(t_range, f_t(t_range).real, f_t(t_range).imag)
  ax1.plot(t_range, f_t(t_range).real, 0)
  ax1.plot(t_range, np.zeros_like(t_range), np.zeros_like(t_range), 'r--')

  ax1.set_xlabel('t')
  ax1.set_ylabel('real')
  ax1.set_zlabel('imaginary')
  ax1.set_title("3D Exponential")

  ax1.legend(["$e^{it}$", "$real(e^{it})$", "x-axis"], loc="upper right")

  return


def oscillator_projections() -> None:
  max = 8 * np.pi
  step = max / 99
  t_range = np.arange(0, max + step, step)

  f_t = lambda t: np.e ** (t * 1j)

  fig = plt.figure(figsize=(10, 5))

  ax1 = fig.add_subplot(2, 2, 1, projection='3d')
  ax1.plot(t_range, f_t(t_range).real, 0)
  ax1.plot(t_range, f_t(t_range).real, f_t(t_range).imag)
  ax1.plot(t_range, np.zeros_like(t_range), np.zeros_like(t_range), 'r--')

  ax1.set_xlabel('t')
  ax1.set_ylabel('real')
  ax1.set_zlabel('imaginary')
  ax1.set_title("3D Exponential")

  ax2 = fig.add_subplot(2, 2, 2)
  ax2.plot(f_t(t_range).real, f_t(t_range).imag)
  ax2.set_aspect("equal")
  ax2.set_xlabel("Real")
  ax2.set_ylabel("Imaginary")
  ax2.set_title("Projection on real-imaginary plane")

  ax3 = fig.add_subplot(2, 2, 3)
  ax3.plot(t_range, f_t(t_range).real)
  ax3.set_aspect("equal")
  ax3.set_xlabel("t")
  ax3.set_ylabel("real")
  ax3.set_title("Projection of the real part")

  ax4 = fig.add_subplot(2, 2, 4)
  ax4.plot(t_range, f_t(t_range).real)
  ax4.plot(t_range, np.cos(t_range), 'r--')

  ax4.set_aspect("equal")
  ax4.set_xlabel("t")
  ax4.set_ylabel("real")
  ax4.set_title("Projection of the real part")

  ax4.legend(["$real(e^{it})$", "$\cos(t)$"], loc="upper right")

  plt.tight_layout()
  plt.show()
  return


def damped_threeD_plot() -> None:
  max = 8 * np.pi
  step = max / 99
  t_range = np.arange(0, max + step, step)

  f_t = lambda t: np.e ** (t * 1j) * np.e ** (-0.1 * t)
  fig = plt.figure()
  ax1 = fig.add_subplot(projection='3d')
  ax1.plot(t_range, f_t(t_range).real, 0)
  ax1.plot(t_range, f_t(t_range).real, f_t(t_range).imag)
  ax1.plot(t_range, np.zeros_like(t_range), np.zeros_like(t_range), 'r--')

  ax1.set_xlabel('t')
  ax1.set_ylabel('real')
  ax1.set_zlabel('imaginary')
  ax1.set_title("3D Damped Exponential")

  return


def damped_oscillator() -> None:
  max = 8 * np.pi
  step = max / 99
  t_range = np.arange(0, max + step, step)

  f_t = lambda t: np.e ** (t * 1j) * np.e ** (-0.1 * t)

  fig = plt.figure(figsize=(10, 5))

  ax1 = fig.add_subplot(2, 2, 1, projection='3d')
  ax1.plot(t_range, f_t(t_range).real, 0)
  ax1.plot(t_range, f_t(t_range).real, f_t(t_range).imag)
  ax1.plot(t_range, np.zeros_like(t_range), np.zeros_like(t_range), 'r--')

  ax1.set_xlabel('t')
  ax1.set_ylabel('real')
  ax1.set_zlabel('imaginary')
  ax1.set_title("3D Damped Exponential")

  ax2 = fig.add_subplot(2, 2, 2)
  ax2.plot(f_t(t_range).real, f_t(t_range).imag)
  ax2.set_aspect("equal")
  ax2.set_xlabel("Real")
  ax2.set_ylabel("Imaginary")
  ax2.set_title("Projection on real-imaginary plane")

  ax3 = fig.add_subplot(2, 2, 3)
  ax3.plot(t_range, f_t(t_range).real)
  ax3.set_aspect("equal")
  ax3.set_xlabel("t")
  ax3.set_ylabel("real")
  ax3.set_title("Projection of the real part")

  ax4 = fig.add_subplot(2, 2, 4)
  ax4.plot(t_range, f_t(t_range).real)
  ax4.plot(t_range, np.cos(t_range) * np.e ** (-0.1 * t_range), 'r--')

  ax4.set_aspect("equal")
  ax4.set_xlabel("t")
  ax4.set_ylabel("real")
  ax4.set_title("Projection of the real part")

  # add a legend for ax4
  ax4.legend(["$real(e^{it}e^{-0.1t})$", "$\cos(t)e^{-0.1t}$"], loc="upper right")

  plt.tight_layout()
  plt.show()
  return
  

def interactive_damped_oscillator() -> None:
  max = 8 * np.pi
  step = max / 99
  t_range = np.arange(0, max + step, step)

  f_t = lambda t, d, w: np.e ** (t * 1j * w) * np.e ** (-d * t)

  fig, ax = plt.subplots(figsize=(10, 5))
  plt.subplots_adjust(left=0.25, bottom=0.25)

  l, = plt.plot(t_range, f_t(t_range, 0.1, 1.0).real)
  l2, = plt.plot(t_range, np.cos(t_range * 1.0) * np.e ** (-0.1 * t_range), 'r--')

  ax.margins(x=0)

  ax_d = plt.axes([0.25, 0.1, 0.65, 0.03])
  s_d = Slider(ax_d, 'Damping', 0.01, 0.5, valinit=0.1)

  ax_w = plt.axes([0.25, 0.15, 0.65, 0.03])
  s_w = Slider(ax_w, 'Angular Frequency', 0.1, 2.0, valinit=1.0)

  def update(val):
    d = s_d.val
    w = s_w.val
    l.set_ydata(f_t(t_range, d, w).real)
    l2.set_ydata(np.cos(t_range * w) * np.e ** (-d * t_range))
    fig.canvas.draw_idle()

  s_d.on_changed(update)
  s_w.on_changed(update)

  ax.set_xlabel("t")
  ax.set_ylabel("real")
  ax.set_title("Projection of the real part")

  ax.legend(["$real(e^{it}e^{-dt})$", "$\cos(t)e^{-dt}$"], loc="upper right")

  plt.show()

  return


def interactive_damped_oscillator_full() -> None:
  max = 8 * np.pi
  step = max / 99
  t_range = np.arange(0, max + step, step)

  f_t = lambda t, d, w: np.e ** (t * 1j * w) * np.e ** (-d * t)

  fig = plt.figure(figsize=(10, 5))
  plt.subplots_adjust(left=0.25, bottom=0.25)

  ax1 = fig.add_subplot(2, 2, 1, projection='3d')
  line1, = ax1.plot(t_range, f_t(t_range, 0.1, 1.0).real, 0)
  line2, = ax1.plot(t_range, f_t(t_range, 0.1, 1.0).real, f_t(t_range, 0.1, 1.0).imag)
  line3, = ax1.plot(t_range, np.zeros_like(t_range), np.zeros_like(t_range), 'r--')

  ax1.set_xlabel('t')
  ax1.set_ylabel('real')
  ax1.set_zlabel('imaginary')
  ax1.set_title("3D Damped Exponential")

  ax2 = fig.add_subplot(2, 2, 2)
  line4, = ax2.plot(f_t(t_range, 0.1, 1.0).real, f_t(t_range, 0.1, 1.0).imag)
  ax2.set_aspect("equal")
  ax2.set_xlabel("Real")
  ax2.set_ylabel("Imaginary")
  ax2.set_title("Projection on real-imaginary plane")

  ax3 = fig.add_subplot(2, 2, 3)
  line5, = ax3.plot(t_range, f_t(t_range, 0.1, 1.0).real)
  ax3.set_aspect("equal")
  ax3.set_xlabel("t")
  ax3.set_ylabel("real")
  ax3.set_title("Projection of the real part")

  ax4 = fig.add_subplot(2, 2, 4)
  line6, = ax4.plot(t_range, f_t(t_range, 0.1, 1.0).real)
  line7, = ax4.plot(t_range, np.cos(t_range * 1.0) * np.e ** (-0.1 * t_range), 'r--')
  ax4.set_aspect("equal")
  ax4.set_xlabel("t")
  ax4.set_ylabel("real")
  ax4.set_title("Projection of the real part")
  ax4.legend(["$real(e^{it}e^{-dt})$", "$\cos(t)e^{-dt}$"], loc="upper right")
  plt.tight_layout()
  plt.subplots_adjust(left=0.25, bottom=0.25)
  ax_d = plt.axes([0.25, 0.1, 0.65, 0.03])
  s_d = Slider(ax_d, 'Damping', 0.01, 0.5, valinit=0.1)
  ax_w = plt.axes([0.25, 0.15, 0.65, 0.03])
  s_w = Slider(ax_w, 'Angular Frequency', 0.1, 2.0, valinit=1.0)  


  def update(val):
    d = s_d.val
    w = s_w.val
    line1.set_data_3d(t_range, f_t(t_range, d, w).real, np.zeros_like(t_range))
    line2.set_data_3d(t_range, f_t(t_range, d, w).real, f_t(t_range, d, w).imag)
    line4.set_xdata(f_t(t_range, d, w).real)
    line4.set_ydata(f_t(t_range, d, w).imag)
    line5.set_ydata(f_t(t_range, d, w).real)
    line6.set_ydata(f_t(t_range, d, w).real)
    line7.set_ydata(np.cos(t_range * w) * np.e ** (-d * t_range))
    fig.canvas.draw_idle()



  s_d.on_changed(update)
  s_w.on_changed(update)

  plt.show()


if __name__ == "__main__":
  unit_circle()
  oscillator_threeD_plot()
  oscillator_projections()
  damped_threeD_plot()
  damped_oscillator()
  interactive_damped_oscillator()
  interactive_damped_oscillator_full()