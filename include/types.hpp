#pragma once

#include <cstdint>

struct WheelReading {
    std::int64_t timestamp_us;
    double left_mps;
    double right_mps;
};

struct HeadingReading {
    std::int64_t timestamp_us;
    double heading_rad;
};

struct Pose {
    double x_m;
    double y_m;
    double theta_rad;
};
