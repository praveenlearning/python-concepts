import re
from datetime import datetime
from typing import List


class Log:
    def __init__(self, timestamp: str, level: str, message: str, date_format: str):
        self.timestamp = datetime.strptime(timestamp, date_format)
        self.level = level
        self.message = message


Logs = List[Log]


class LogParser:
    def __init__(self, log_format: str, fallback_format: str, date_format: str):
        self.log_format = log_format
        self.fallback_format = fallback_format
        self.date_format = date_format

    def parse(self, data) -> Logs:
        logs: Logs = []
        pattern = re.compile(self.log_format)
        fallback = re.compile(self.fallback_format)
        for line in data:
            search = pattern.search(line)
            if search is None:
                message, *_ = fallback.search(line).groups()
                logs[-1].message += message
            else:
                timestamp, log_level, message = search.groups()
                log = Log(timestamp, log_level, message, self.date_format)
                logs.append(log)
        return logs


# class SyncLogParser(LogParser):
#     @staticmethod
#     def parse(data) -> Logs:
#         logs: Logs = []
#         for line in data:
#             data: List[str] = line.split(" | ")
#             if len(data) < 3:
#                 last_updated: Log = logs[-1]
#                 last_updated.message += line
#             else:
#                 timestamp, level, *_, message = line.split(" | ")
#                 logs.append(
#                     Log(timestamp=timestamp, level=level, message=message, date_format="%Y-%m-%dT%H:%M:%S,%f %z"))
#         return logs
#
#
# class DockerLogParser(LogParser):
#     @staticmethod
#     def parse(data) -> Logs:
#         logs: Logs = []
#         for line in data:
#             pattern: re.Pattern = re.compile(r"(\w{3} \d{2} \d{2}:\d{2}:\d{2}).*(DEBUG|INFO|WARN|ERROR)[^a-zA-Z]+(.*)")
#             search: re.Match = pattern.search(line)
#             if search is None:
#                 *_, message = line.split(": ")
#                 logs[-1].message += message
#             else:
#                 timestamp, level, message = search.groups()
#                 Log(timestamp=timestamp, level=level, message=message, date_format="%b %d %H:%M:S")
#
#         return logs


# test = "2022-12-21T00:07:25,200 +1100 | INFO |  |  |  | [RunUploads] --START-- Term code: 2019.1RT S1"
# pattern = re.compile(r"([A-Z0-9:,+ \-]*) \| ([A-Z]*) \|.* \| (.*)")

# test = "Dec 21 16:55:49 preprod3 docker/sync-runner[11146]: main - INFO * Processing request"
# pattern = re.compile(r"([a-zA-Z]{3} [0-9: ]*) .*: .* - ([A-Z]*) (.*)")
#
# print(pattern.match(test).groups())
#
# test2 = "Dec 21 16:56:00 preprod3 docker/sync-runner[11146]: Database connections closed"
# fallback = re.compile(r".*: (.*)")
# print(fallback.search(test2).groups())
#
# test3 = "	at net.sourceforge.jtds.jdbc.JtdsConnection.<init>(JtdsConnection.java:427)\n"
# fallback = re.compile("(.432)")
# print(fallback.search(test3).groups())
#

test = "2022-12-21T00:07:25,200 +1100 | INFO |  |  |  | [RunUploads] --START-- Term code: 2019.1RT S1"
pattern = re.compile(r"([A-Z0-9:,+ \-]*).*(DEBUG|INFO|WARN|ERROR).*\| (.*)")
print(pattern.search(test).groups())
