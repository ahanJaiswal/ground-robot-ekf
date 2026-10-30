#include "csv_reader.hpp"

// TODO: Implement CSV loading here.
// Both files have no header row.
// wheels.csv: timestamp_us,left_mps,right_mps
// kvh.csv: timestamp_us,heading_rad
// Keep timestamps as 64-bit integers and check for invalid rows.

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdint>



using namespace std;

struct WheelReading {
    int64_t timestamp_us;
    double left_mps;
    double right_mps;
};

struct HeadingReading {
    int64_t timestamp_us;
    double heading;
};

int main() {
    // use wheels.csv timestamps, use left/right wheel speed into vector
    // use kvh.csv with latest heading for correlating wheel timestamp, put that into headingreading vector
   
    vector<WheelReading> wheel_readings;
    wheel_readings.reserve(250000);

    vector<HeadingReading> heading_readings;
    heading_readings.reserve(250000);

    
    ifstream wheels_file;
    wheels_file.open("/home/ahan-jaiswal/Documents/ground-robot-ekf/data/raw/2012-01-08/2012-01-08_sen/2012-01-08/wheels.csv");
    ifstream kvh_file;
    kvh_file.open("/home/ahan-jaiswal/Documents/ground-robot-ekf/data/raw/2012-01-08/2012-01-08_sen/2012-01-08/kvh.csv");
    

    for (string wheels_line; getline(wheels_file, wheels_line); ) {

        string::size_type pos = wheels_line.find(',');
        string timestamp = wheels_line.substr(0, pos);
        string left_mps = wheels_line.substr(pos+1, wheels_line.substr(pos+1).find(','));
        string right_mps = wheels_line.substr(timestamp.length() + left_mps.length() + 2);

        WheelReading reading;
        reading.timestamp_us = stoll(timestamp);
        reading.left_mps = stod(left_mps);
        reading.right_mps = stod(right_mps);

        wheel_readings.push_back(reading);
    }

    for (string kvh_line; getline(kvh_file, kvh_line);) {
        string::size_type pos = kvh_line.find(',');
        string timestamp = kvh_line.substr(0, pos);
        string heading = kvh_line.substr(pos + 1);

        HeadingReading reading;
        reading.timestamp_us = stoll(timestamp);
        reading.heading = stod(heading);

        heading_readings.push_back(reading);
    }

    return 0;
}