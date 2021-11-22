import re
from datetime import datetime

class Record:
    def __init__(self, num, channel_id, timestamp, group):
        self.num = num
        self.channel_id = channel_id
        self.timestamp = timestamp
        self.group = group

    @staticmethod
    def parse(text):
        result = re.search(r'\d{4} \w{2} \d{2}:\d{2}:\d{2}.\d{3} \d{2}\r', text)  # add \r ?

        if result:
            found = result.group(0)
            timestamp = datetime.strptime(found[8:20], "%H:%M:%S.%f")
            return Record(found[0:4], found[5:7], timestamp, int(found[21:23]))
        else:
            return None

    def to_text(self):
        text = 'спортсмен, нагрудный номер {} прошёл отсечку {} в {}'
        return text.format(self.num, self.channel_id, self.timestamp.strftime("%H:%M:%S.%f")[:-5])