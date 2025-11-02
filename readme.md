#  Homogeneous Transformation Matrix (HTM) Operations

This project provides a robust set of Python functions, utilizing `NumPy` and `Matplotlib`, to manage 3D rigid body transformations (rotation and translation). These concepts are fundamental in robotics, computer graphics, and spatial mechanics.

##  Features and Functions

| Function Name | Description |
| :--- | :--- |
| **`homogeneous_matrix(R, p)`** | Constructs the $4 \times 4$ Homogeneous Transformation Matrix ($T$) from a $3 \times 3$ Rotation Matrix ($R$) and a $3 \times 1$ Position Vector ($p$). |
| **`hom_inverse(T)`** | Calculates the efficient analytical inverse of the Homogeneous Transformation Matrix ($T^{-1}$), which represents the inverse transformation. |
| **`rot_z(angle)`** | Generates the $3 \times 3$ Rotation Matrix for a rotation about the Z-axis, given an angle in degrees. |
| **`plot_coordinate_system`** | Visualizes the transformation by plotting the **Fixed Frame** (World) and the **Mobile Frame** (Transformed System) in 3D space. |

##  Prerequisites

To run this code, you must have Python installed along with the following libraries:

```bash
pip install numpy matplotlib

Mathematical Structure
The Homogeneous Transformation Matrix T is constructed with the following block structure:

$$T = \begin{pmatrix} R & p \\ \mathbf{0} & 1 \end{pmatrix} $$ * $R$: The $3 \times 3$ Rotation Matrix (Orientation). * $p$: The $3 \times 1$ Position Vector (Translation). * $\mathbf{0}$: The $1 \times 3$ zero vector $\begin{pmatrix} 0 & 0 & 0 \end{pmatrix}$. Given that $R$ is an orthogonal matrix, the inverse transformation $T^{-1}$ is calculated efficiently as: $$T^{-1} = \begin{pmatrix} R^T & -R^T p \\ \mathbf{0} & 1 \end{pmatrix} $$\#\#  Usage Example The following code demonstrates defining a transformation ($90^\circ$ Z-rotation and a translation of $(5, 2, 8)$), calculating $T$ and $T^{-1}$, and visualizing the frames. ```python # Import libraries and define functions (homogeneous_matrix, rot_z, etc.) above... # 1. Define Transformation Parameters (Z-rotation by 90 degrees, translation (5, 2, 8)) matrix = rot_z(90) vector = np.array([5, 2, 8]) # 2. Calculate T and T^-1 Matrices homogen_matrix = homogeneous_matrix(matrix, vector) inverse_matrix = hom_inverse(homogen_matrix) print("Homogeneous Transformation Matrix (T):\n", homogen_matrix) print("\nInverse Transformation Matrix (T^-1):\n", inverse_matrix) # 3. 3D Visualization Setup fig = plt.figure(figsize=(10, 8)) ax = fig.add_subplot(111, projection='3d') # a) Fixed Frame (World System) plot_coordinate_system(ax, np.identity(3), np.array([0, 0, 0]), 'Fixed (A)', scale=2) # b) Transformed Frame (Mobile System) R_B = homogen_matrix[:3, :3] p_B = homogen_matrix[:3, 3] plot_coordinate_system(ax, R_B, p_B, 'Mobile (B)', scale=2) # c) Graph Settings max_coord = max(np.max(np.abs(p_B)) + 2, 3) ax.set_xlim([-max_coord, max_coord]) ax.set_ylim([-max_coord, max_coord]) ax.set_zlim([-max_coord, max_coord]) ax.set_title(r'Homogeneous Transformation ($T_{A \to B}$)') ax.legend() plt.show() ```$$