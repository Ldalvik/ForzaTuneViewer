#include "stdint.h"

typedef struct
{
    float aero_front;
    float aero_rear;
    float final_drive;
    float brake_pressure;
    float brake_balance;
    float torque_split;
    float power_bias;
    float unknown3;
    float unknown4;
    float unknown5;
    float unknown6;
    float unknown7;
    float tire_pressure_front;
    float camber_front;
    float toe_front;
    float caster_front;
    float springs_front;
    float arbs_front;
    float ride_height_front;
    float bump_front;
    float rebound_front;
    float accel_front;
    float decel_front;
    float tire_pressure_rear;
    float camber_rear;
    float toe_rear;
    float unknown8;
    float springs_rear;
    float arbs_rear;
    float ride_height_rear;
    float bump_rear;
    float rebound_rear;
    float accel_rear;
    float decel_rear;
    float unknown9;
    float unknown10;
    float first_gear;
    float second_gear;
    float third_gear;
    float fourth_gear;
    float fifth_gear;
    float sixth_gear;
    float seventh_gear;
    float eighth_gear;
    float ninth_gear;
    float tenth_gear;
} TuningSection;

typedef struct 
{
    uint32_t rims;
    uint32_t engine;
    uint32_t drivetrain;
    uint32_t carbody;
    uint32_t motor;
    uint32_t brakes;
    uint32_t springs;
    uint32_t arbs_front;
    uint32_t arbs_rear;
    uint32_t tire_compound;
    uint32_t wing_rear;
    uint32_t rim_size_front;
    uint32_t rim_size_rear;
    uint32_t camshaft;
    uint32_t valves;
    uint32_t displacement;
    uint32_t piston_compression;
    uint32_t fuel_system;
    uint32_t ignition;
    uint32_t exhaust;
    uint32_t intake;
    uint32_t flywheel;
    uint32_t manifold;
    uint32_t restrictor_plate;
    uint32_t oil_cooling;
    uint32_t single_turbo;
    uint32_t twin_turbo;
    uint32_t quad_turbo;
    uint32_t csc_supercharger;
    uint32_t dsc_supercharger;
    uint32_t intercooler;
    uint32_t clutch;
    uint32_t transmission;
    uint32_t driveline;
    uint32_t differential;
    uint32_t bumper_front;
    uint32_t bumper_rear;
    uint32_t hood;
    uint32_t side_skirts;
    uint32_t tire_width_front;
    uint32_t tire_width_rear;
    uint32_t weight_reduction;
    uint32_t chassis_stiffness;
    uint32_t unknown2;
    uint32_t track_spacing_front;
    uint32_t track_spacing_rear;
    // uint32_t tire_profile_size_front;
    // uint32_t tire_profile_size_rear;
} UpgradesSection;

typedef struct
{
    uint16_t version;
    uint32_t ordinal;
    uint32_t unknown1;
} Metadata;

typedef struct
{
    Metadata metadata;
    UpgradesSection upgrades;
    TuningSection tuning;
} __attribute__((__packed__)) TuneFile;
