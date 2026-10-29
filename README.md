# Ground Robot EKF

A C++ project for ground-robot state estimation using wheel velocities, gyro/IMU measurements, and GPS recordings from the University of Michigan NCLT dataset.

## Current status

The repository contains a buildable C++17 scaffold and a local copy of the first dataset session. Dataset loading, filtering, and evaluation are not implemented yet.

## First deliverable

- Load and inspect the 2012-01-08 NCLT recording.
- Implement wheel/gyro dead reckoning as a baseline.
- Implement an extended Kalman filter combining wheel velocity, gyro, and GPS measurements.
- Plot estimated and reference trajectories and report position error.
- Document how to build and reproduce the results.

Slip-aware estimation and ROS 2 integration are later extensions.

## Repository layout

```text
src/             C++ implementation and executable entry point
include/         C++ headers
scripts/         Python data inspection and plotting utilities
config/          Filter and experiment configuration
results/         Generated plots and metrics (ignored by Git)
data/raw/        Downloaded recordings (ignored by Git)
```

## Build and run

Requirements: a C++17 compiler and CMake 3.16 or newer.

```bash
cmake -S . -B build
cmake --build build
./build/ground_robot_ekf
```

The executable currently prints a scaffold status message; it does not process data yet.

## Dataset

Source: [University of Michigan North Campus Long-Term Dataset](https://robots.engin.umich.edu/nclt/index.html).

Start with session `2012-01-08`: its sensor archive, reference trajectory, and reference covariance. Camera and LiDAR downloads are not required for the first deliverable.

Local layout (the sensor archive's extracted folder structure is preserved):

```text
data/raw/2012-01-08/
├── 2012-01-08_sen.tar.gz
├── groundtruth_2012-01-08.csv
├── cov_2012-01-08.csv
└── 2012-01-08_sen/
    └── 2012-01-08/
        ├── README.txt
        ├── wheels.csv
        ├── kvh.csv
        ├── ms25.csv
        ├── gps.csv
        └── ...
```

Keep reference trajectories separate from estimator inputs. NCLT's reference poses were generated using a SLAM graph and interpolated using odometry; evaluation must account for this dependence. The project does not yet claim measured localization improvements or validated physical slip estimates.

The dataset uses the Open Database License and Database Contents License; see the source website for terms. Raw recordings are excluded from this repository.

Dataset citation: Nicholas Carlevaris-Bianco, Arash K. Ushani, and Ryan M. Eustice, *University of Michigan North Campus Long-Term Vision and Lidar Dataset*, International Journal of Robotics Research, 2016.
