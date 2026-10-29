#include "dead_reckoning.hpp"

// TODO: Implement timestamp matching and position updates here.
// Match each wheel timestamp to the latest available heading at or before it.
// Skip wheel samples before the first heading; check for stale headings.
// Convert timestamp differences from microseconds to seconds.
// Start at local pose (0, 0, 0), using the initial heading as a reference.
// Wrap heading differences and check the dataset's heading sign convention.
// For each interval, use the previous wheel speed and previous local heading.
