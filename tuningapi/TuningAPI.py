import struct
import os
from tuningapi.Metadata import Metadata
from tuningapi.UpgradeData import UpgradeData
from tuningapi.TuningData import TuningData

FORZA_PATH = os.path.expanduser('~') + "/AppData/Local/Packages/Microsoft.624F8B84B80_8wekyb3d8bbwe"
TUNE_FILES_PATH = FORZA_PATH + "/SystemAppData/wgs"

class TuningAPI:
    def __init__(self):
        self.current_tune = {}
        self.all_tunes = []

    def load_tune_by_id(self, tune_id):
        for tune in self.all_tunes:
            if tune['id'] == tune_id:
                self.load_tune(tune)
                break

    def load_tune_by_index(self, index):
        self.load_tune(self.all_tunes[index])

    def load_tune(self, tune):
        data = tune['data']
        tune_version = struct.unpack('B', data[:1])[0]
      
        upgrade_size = 46 if tune_version == 2 else 48
        upgrade_bytes = struct.unpack(f'<{upgrade_size}I', data[10:10 + upgrade_size])
        tuning_bytes = struct.unpack('<46f', data[10 + upgrade_size:])

        self.current_tune = {
            'path': tune['path'],
            'version': tune_version,
            'ordinal': tune['ordinal'],
            'tuning': TuningData(list(tuning_bytes)),
            'upgrades': UpgradeData(list(upgrade_bytes)),
            'metadata': tune['metadata']
        }

    def find_tunes(self, folder=None):
        folder = folder or TUNE_FILES_PATH
        files = os.listdir(folder)
        file_dir = os.path.join(folder, file_name)
        file_size = os.path.getsize(file_dir)

        for file_name in files:
            if os.path.isdir(file_dir):
                self.find_tunes(file_dir)
            elif os.path.isfile(file_dir):
                if file_size in {378, 386}:
                    with open(file_dir, 'rb') as file:
                        tune_data = file.read()
                        if tune_data[0] in {2, 3}:
                            ordinal = struct.unpack('<I', tune_data[2:6])[0]
                            self.all_tunes.append({
                                'tune_id': os.path.basename(file_dir),
                                'ordinal': ordinal,
                                'path': os.path.dirname(file_dir),
                                'data': tune_data,
                                'metadata': Metadata(self.find_metadata(os.path.dirname(file_dir)))
                            })
                        else:
                            print(f'Unsupported tune file version (v={tune_data[0]})')

    def find_metadata(self, tune_path):
        for file_name in os.listdir(tune_path):
            file_path = os.path.join(tune_path, file_name)

            with open(file_path, 'rb') as file:
                file_data = file.read()

            if 'container' not in file_name and file_data[0] in {0x04, 0x06}:
                return file_data

        return None
            
