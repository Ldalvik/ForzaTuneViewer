import struct

class Metadata:
    def __init__(self, file_data):
        self.file_data = file_data
        self.title_offset = 8
        self.title_length = self.read_value(4)
        self.description_offset = self.title_offset + self.title_length + 4
        self.description_length = self.read_value(self.title_offset + self.title_length)
        self.upload_date_offset = self.description_offset + self.description_length
        self.gamertag_offset = self.upload_date_offset + 32
        self.gamertag_length = self.read_value(self.gamertag_offset - 4)

    def read_value(self, offset):
        return struct.unpack('<B', self.file_data[offset:offset + 1])[0] * 2

    def get_title(self):
        return self.get_string_from_bytes(self.title_offset, self.title_length)

    def get_description(self):
        return self.get_string_from_bytes(self.description_offset, self.description_length)

    def get_upload_date(self):
        year = struct.unpack('<H', self.file_data[self.upload_date_offset:self.upload_date_offset + 2])[0]
        month = struct.unpack('<H', self.file_data[self.upload_date_offset + 4:self.upload_date_offset + 6])[0]
        day = struct.unpack('<H', self.file_data[self.upload_date_offset + 8:self.upload_date_offset + 10])[0]

        return f"{month + 1}/{day + 1}/{year}"

    def get_gamertag(self):
        return self.get_string_from_bytes(self.gamertag_offset, self.gamertag_length)

    def get_string_from_bytes(self, offset, length):
        string_bytes = self.file_data[offset:offset + length]
        string_code_units = struct.unpack(f'<{length // 2}H', string_bytes)
        return ''.join(map(chr, string_code_units))
