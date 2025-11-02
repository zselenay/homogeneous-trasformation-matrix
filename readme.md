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
## 📐 Mathematical Structure (Simplified)

The Homogeneous Transformation Matrix T is constructed with the following block structure:

T = | R | p |
    | 0 | 1 |

Where:
* R is the 3x3 Rotation Matrix (Orientation).
* p is the 3x1 Position Vector (Translation).
* 0 is the 1x3 zero vector (0 0 0).

Since R is an orthogonal matrix, the inverse transformation T^-1 is calculated efficiently as:

T^-1 = | R^T | -R^T * p |
       | 0   | 1        |
