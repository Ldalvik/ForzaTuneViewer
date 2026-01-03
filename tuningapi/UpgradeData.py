from tuningapi.Schema import Upgrades

class UpgradeData:
    def __init__(self, upgradeBytes):
        self.upgradeBytes = upgradeBytes

    @property
    def rims(self):
        return self.upgradeBytes[Upgrades.RIMS.value]

    @property
    def engine(self):
        return self.read(Upgrades.ENGINE)

    @property
    def drivetrain(self):
        return self.read(Upgrades.DRIVETRAIN)

    @property
    def carbody(self):
        return self.read(Upgrades.CARBODY)

    @property
    def motor(self):
        return self.read(Upgrades.MOTOR)

    @property
    def brakes(self):
        return self.read(Upgrades.BRAKES)

    @property
    def springs(self):
        return self.read(Upgrades.SPRINGS)

    @property
    def arbs_front(self):
        return self.read(Upgrades.ARBS_FRONT)

    @property
    def arbs_rear(self):
        return self.read(Upgrades.ARBS_REAR)

    @property
    def tire_compound(self):
        return self.read(Upgrades.TIRE_COMPOUND)

    @property
    def wing_rear(self):
        return self.read(Upgrades.WING_REAR)

    @property
    def rim_size_front(self):
        return self.read(Upgrades.RIM_SIZE_FRONT)

    @property
    def rim_size_rear(self):
        return self.read(Upgrades.RIM_SIZE_REAR)

    @property
    def camshaft(self):
        return self.read(Upgrades.CAMSHAFT)

    @property
    def valves(self):
        return self.read(Upgrades.VALVES)

    @property
    def displacement(self):
        return self.read(Upgrades.DISPLACEMENT)

    @property
    def piston_compression(self):
        return self.read(Upgrades.PISTON_COMPRESSION)

    @property
    def fuel_system(self):
        return self.read(Upgrades.FUEL_SYSTEM)

    @property
    def ignition(self):
        return self.read(Upgrades.IGNITION)

    @property
    def exhaust(self):
        return self.read(Upgrades.EXHAUST)

    @property
    def intake(self):
        return self.read(Upgrades.INTAKE)

    @property
    def flywheel(self):
        return self.read(Upgrades.FLYWHEEL)

    @property
    def manifold(self):
        return self.read(Upgrades.MANIFOLD)

    @property
    def restrictor_plate(self):
        return self.read(Upgrades.RESTRICTOR_PLATE)

    @property
    def oil_cooling(self):
        return self.read(Upgrades.OIL_COOLING)

    @property
    def single_turbo(self):
        return self.read(Upgrades.SINGLE_TURBO)

    @property
    def twin_turbo(self):
        return self.read(Upgrades.TWIN_TURBO)

    @property
    def quad_turbo(self):
        return self.read(Upgrades.QUAD_TURBO)

    @property
    def csc_supercharger(self):
        return self.read(Upgrades.CSC_SUPERCHARGER)

    @property
    def dsc_supercharger(self):
        return self.read(Upgrades.DSC_SUPERCHARGER)

    @property
    def intercooler(self):
        return self.read(Upgrades.INTERCOOLER)

    @property
    def clutch(self):
        return self.read(Upgrades.CLUTCH)

    @property
    def transmission(self):
        return self.read(Upgrades.TRANSMISSION)

    @property
    def driveline(self):
        return self.read(Upgrades.DRIVELINE)

    @property
    def differential(self):
        return self.read(Upgrades.DIFFERENTIAL)

    @property
    def bumper_front(self):
        return self.read(Upgrades.BUMPER_FRONT)

    @property
    def bumper_rear(self):
        return self.read(Upgrades.BUMPER_REAR)

    @property
    def hood(self):
        return self.read(Upgrades.HOOD)

    @property
    def side_skirts(self):
        return self.read(Upgrades.SIDE_SKIRTS)

    @property
    def tire_width_front(self):
        return self.read(Upgrades.TIRE_WIDTH_FRONT)

    @property
    def tire_width_rear(self):
        return self.read(Upgrades.TIRE_WIDTH_REAR)

    @property
    def weight_reduction(self):
        return self.read(Upgrades.WEIGHT_REDUCTION)

    @property
    def chassis_stiffness(self):
        return self.read(Upgrades.CHASSIS_STIFFNESS)

    @property
    def unknown_2(self):
        return self.read(Upgrades.UNKNOWN_2)

    @property
    def track_spacing_front(self):
        return self.read(Upgrades.TRACK_SPACING_FRONT)

    @property
    def track_spacing_rear(self):
        return self.read(Upgrades.TRACK_SPACING_REAR)

    @property
    def tire_profile_size_front(self):
        return self.read(Upgrades.TIRE_PROFILE_SIZE_FRONT)

    @property
    def tire_profile_size_rear(self):
        return self.read(Upgrades.TIRE_PROFILE_SIZE_REAR)

    # setters
    @rims.setter
    def rims(self, value):
        self.upgradeBytes[Upgrades.RIMS.value] = value

    @engine.setter
    def engine(self, value):
        self.write(Upgrades.ENGINE, value)

    @drivetrain.setter
    def drivetrain(self, value):
        self.write(Upgrades.DRIVETRAIN, value)

    @carbody.setter
    def carbody(self, value):
        self.write(Upgrades.CARBODY, value)

    @motor.setter
    def motor(self, value):
        self.write(Upgrades.MOTOR, value)

    @brakes.setter
    def brakes(self, value):
        self.write(Upgrades.BRAKES, value)

    @springs.setter
    def springs(self, value):
        self.write(Upgrades.SPRINGS, value)

    @arbs_front.setter
    def arbs_front(self, value):
        self.write(Upgrades.ARBS_FRONT, value)

    @arbs_rear.setter
    def arbs_rear(self, value):
        self.write(Upgrades.ARBS_REAR, value)

    @tire_compound.setter
    def tire_compound(self, value):
        self.write(Upgrades.TIRE_COMPOUND, value)

    @wing_rear.setter
    def wing_rear(self, value):
        self.write(Upgrades.WING_REAR, value)

    @rim_size_front.setter
    def rim_size_front(self, value):
        self.write(Upgrades.RIM_SIZE_FRONT, value)

    @rim_size_rear.setter
    def rim_size_rear(self, value):
        self.write(Upgrades.RIM_SIZE_REAR, value)

    @camshaft.setter
    def camshaft(self, value):
        self.write(Upgrades.CAMSHAFT, value)

    @valves.setter
    def valves(self, value):
        self.write(Upgrades.VALVES, value)

    @displacement.setter
    def displacement(self, value):
        self.write(Upgrades.DISPLACEMENT, value)

    @piston_compression.setter
    def piston_compression(self, value):
        self.write(Upgrades.PISTON_COMPRESSION, value)

    @fuel_system.setter
    def fuel_system(self, value):
        self.write(Upgrades.FUEL_SYSTEM, value)

    @ignition.setter
    def ignition(self, value):
        self.write(Upgrades.IGNITION, value)

    @exhaust.setter
    def exhaust(self, value):
        self.write(Upgrades.EXHAUST, value)

    @intake.setter
    def intake(self, value):
        self.write(Upgrades.INTAKE, value)

    @flywheel.setter
    def flywheel(self, value):
        self.write(Upgrades.FLYWHEEL, value)

    @manifold.setter
    def manifold(self, value):
        self.write(Upgrades.MANIFOLD, value)

    @restrictor_plate.setter
    def restrictor_plate(self, value):
        self.write(Upgrades.RESTRICTOR_PLATE, value)

    @oil_cooling.setter
    def oil_cooling(self, value):
        self.write(Upgrades.OIL_COOLING, value)

    @single_turbo.setter
    def single_turbo(self, value):
        self.write(Upgrades.SINGLE_TURBO, value)

    @twin_turbo.setter
    def twin_turbo(self, value):
        self.write(Upgrades.TWIN_TURBO, value)

    @quad_turbo.setter
    def quad_turbo(self, value):
        self.write(Upgrades.QUAD_TURBO, value)

    @csc_supercharger.setter
    def csc_supercharger(self, value):
        self.write(Upgrades.CSC_SUPERCHARGER, value)

    @dsc_supercharger.setter
    def dsc_supercharger(self, value):
        self.write(Upgrades.DSC_SUPERCHARGER, value)

    @intercooler.setter
    def intercooler(self, value):
        self.write(Upgrades.INTERCOOLER, value)

    @clutch.setter
    def clutch(self, value):
        self.write(Upgrades.CLUTCH, value)

    @transmission.setter
    def transmission(self, value):
        self.write(Upgrades.TRANSMISSION, value)

    @driveline.setter
    def driveline(self, value):
        self.write(Upgrades.DRIVELINE, value)

    @differential.setter
    def differential(self, value):
        self.write(Upgrades.DIFFERENTIAL, value)

    @bumper_front.setter
    def bumper_front(self, value):
        self.write(Upgrades.BUMPER_FRONT, value)

    @bumper_rear.setter
    def bumper_rear(self, value):
        self.write(Upgrades.BUMPER_REAR, value)

    @hood.setter
    def hood(self, value):
        self.write(Upgrades.HOOD, value)

    @side_skirts.setter
    def side_skirts(self, value):
        self.write(Upgrades.SIDE_SKIRTS, value)

    @tire_width_front.setter
    def tire_width_front(self, value):
        self.write(Upgrades.TIRE_WIDTH_FRONT, value)

    @tire_width_rear.setter
    def tire_width_rear(self, value):
        self.write(Upgrades.TIRE_WIDTH_REAR, value)

    @weight_reduction.setter
    def weight_reduction(self, value):
        self.write(Upgrades.WEIGHT_REDUCTION, value)

    @chassis_stiffness.setter
    def chassis_stiffness(self, value):
        self.write(Upgrades.CHASSIS_STIFFNESS, value)

    @unknown_2.setter
    def unknown_2(self, value):
        self.write(Upgrades.UNKNOWN_2, value)

    @track_spacing_front.setter
    def track_spacing_front(self, value):
        self.write(Upgrades.TRACK_SPACING_FRONT, value)

    @track_spacing_rear.setter
    def track_spacing_rear(self, value):
        self.write(Upgrades.TRACK_SPACING_REAR, value)

    @tire_profile_size_rear.setter
    def tire_profile_size_front(self, value):
        self.write(Upgrades.TIRE_PROFILE_SIZE_FRONT, value)

    @tire_profile_size_front.setter
    def tire_profile_size_rear(self,value):
        self.write(Upgrades.TIRE_PROFILE_SIZE_REAR, value)


    def read(self, index):
        data = self.upgradeBytes[index.value]
        return -1 if data == -1 else int(str(data)[-3:])

    def write(self, index, value):
        partKey = str(self.upgradeBytes[index.value])[:3]
        self.upgradeBytes[index] = int(partKey + str(value).zfill(3))