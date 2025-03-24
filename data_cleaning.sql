-- Remove Null Values
DELETE FROM flight_data WHERE landing_count IS NULL OR total_landed_weight IS NULL;

-- Standardize Date Format
UPDATE flight_data
SET activity_period = TO_DATE(activity_period, 'YYYYMM');
