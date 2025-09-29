import matplotlib.pyplot as plt
import numpy as np

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

  # add labels
  plt.text(f_t(0).real, f_t(0).imag, "$0$")
  plt.text(f_t(np.pi/6).real, f_t(np.pi/6).imag, "$\pi/6$")
  plt.text(f_t(np.pi/4).real, f_t(np.pi/4).imag, "$\pi/4$")
  plt.text(f_t(np.pi/3).real, f_t(np.pi/3).imag, "$\pi/3$")
  plt.text(f_t(np.pi/2).real, f_t(np.pi/2).imag, "$\pi/2$")

  # add legend for the functions plotted
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

  # add legend
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

  # add a legend for ax4
  ax4.legend(["$real(e^{it})$", "$\cos(t)$"], loc="upper right")

  plt.tight_layout()
  plt.show()
  return

# function like threeD_plot for a damped oscillator
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


# function like the ones above but for a damped oscillator
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

if __name__ == "__main__":
  unit_circle()
  oscillator_threeD_plot()
  oscillator_projections()
  damped_threeD_plot()
  damped_oscillator()