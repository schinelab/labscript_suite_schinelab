from labscript import *

# adding worker and blacs tab to the imports
from labscript_devices.PulseBlaster_No_DDS import *
from labscript_devices.NI_DAQmx.labscript_devices import NI_PCI_6713
from labscript import start, stop, DigitalOut, ClockLine, Trigger
from labscript_devices.DummyPseudoclock.labscript_devices import DummyPseudoclock
from labscript_devices.DummyIntermediateDevice import DummyIntermediateDevice
from labscript_devices.FlyCapture2Camera.labscript_devices import FlyCapture2Camera
from labscript_devices.GeniCam.labscript_devices import GeniCam
PulseBlaster_No_DDS(name='pulseblaster_0', board_number=0,programming_scheme='pb_start/BRANCH')
#ClockLine(name='pb_clockline_fast', pseudoclock=pulseblaster_0.pseudoclock,connection='flag 4')

mv_cti_file = r'C:\Program Files\Teledyne\Spinnaker\cti64\vs2015\Spinnaker_GenTL_v140.cti'

ClockLine(name='pulseblaster_0_ni_0_clock',	pseudoclock=pulseblaster_0.pseudoclock, connection='flag 0')
DigitalOut(name='Zeeman_slower', parent_device=pulseblaster_0.direct_outputs, connection = 'flag 1')
DigitalOut(name='Blue_2D_MOT', parent_device=pulseblaster_0.direct_outputs, connection = 'flag 2')
DigitalOut(name='probe_beam', parent_device=pulseblaster_0.direct_outputs, connection = 'flag 3')
DigitalOut(name='Blue_3D_MOT', parent_device=pulseblaster_0.direct_outputs, connection = 'flag 4')
DigitalOut(name='Green_Beams', parent_device=pulseblaster_0.direct_outputs, connection = 'flag 6')

DigitalOut(name='start_experiment', parent_device=pulseblaster_0.direct_outputs, connection = 'flag 7')


Trigger(name='cam1_trigger',      parent_device=pulseblaster_0.direct_outputs, connection = 'flag 5', trigger_edge_type = 'rising')


################################################################################
#   NI CARD 
################################################################################

NI_PCI_6713(name='ni_0', parent_device=pulseblaster_0_ni_0_clock, clock_terminal='/Dev1/PFI0', MAX_name = 'Dev1')

AnalogOut(name='MOT_coils_setpoint', parent_device=ni_0, connection='ao0')
AnalogOut(name='MOT_coils_power', parent_device=ni_0, connection='ao1')

################################################################################
#   Camera
################################################################################
cam1_sequence_attributes = {
    "Acquisition Control" : {
#      "Trigger Selector": "FrameStart",
        "Trigger Mode": "On",
        "Trigger Source": "Line0",
        "Trigger Activation": "RisingEdge",
#        "TriggerDelay": 0.0,
#        "TriggerDelayEnabled": "false",
#        "ExposureMode": "Timed",
#        "Exposure Auto": "On",
#        "Exposure Time": 16157.746315002441,
#        "Exposure Compensation Auto": "Continuous",
        "Acquisition Mode": "MultiFrame",
#        "AcquisitionStatusSelector": "FrameTriggerWait",
#        "SingleFrameAcquisition Mode": "FreeRunning",
#        "HighDynamicRangeModeEnabled": "false"
    }
   }


cam1_manual_attributes = {
#    "Analog Control": {
#        "Gain Auto": "Off",
#        "Gain": 0.0,
#        "BlackLevel": 0.0
#    },
    "Acquisition Control": {
#        "TriggerSelector": "FrameStart",
        "Trigger Mode": "On",
        "Trigger Source": "Line0",
        "Trigger Activation": "RisingEdge",
#        "TriggerDelay": 0.0,
#        "TriggerDelayEnabled": "false",
#        "ExposureMode": "Timed",
#        "Exposure Auto": "On",
#        "Exposure Time": 16157.746315002441,
#        "Exposure Compensation Auto": "Continuous",
        "Acquisition Mode": "MultiFrame",
#        "AcquisitionStatusSelector": "FrameTriggerWait",
        "Single Frame Acquisition Mode": "FreeRunning",
#        "HighDynamicRangeModeEnabled": "false"
   },
#    "Image Format Control": {
#        "PixelFormat": "Mono8",
#        "Width": 1920,
#        "Height": 1200,
#        "Offset X": 0,
#        "Offset Y": 0,
#        "Binning Vertical": 1,
#        "Reverse X": "false",
#        "Reverse Y": "false",
#        "TestPattern": "Off",
    },

GeniCam(
    name='cam1',
    cti_file = mv_cti_file,
    parent_device=cam1_trigger,
    connection='trigger',
    serial_number="19123472",
    trigger_edge_type='rising',
    camera_attributes=cam1_sequence_attributes,
    manual_mode_camera_attributes=cam1_manual_attributes,
    manual_acquisition_timeout=5.0,
    stop_acquisition_timeout=50.0
)


if __name__ == '__main__':
    start()
    stop(1)