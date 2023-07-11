import re

from log_parser import SyncLogParser

# print(re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2},\d{3}", "2022-12-21T00:07:25,200"))


# print(datetime(2022, 12, 21, 0, 7, 25, 200, timezone(timedelta(hours=11))))
#
# print(datetime.strptime("2022-12-21T00:07:25,200 +1100", r"%Y-%m-%dT%H:%M:%S,%f %z"))

# pattern = re.compile(r"\w* - (DEBUG|INFO|WARN|ERROR)[^a-zA-Z]+(.*)")
# pattern = re.compile(r"(DEBUG|INFO|WARN|ERROR)[^a-zA-Z]+(.*)")
# pattern = re.compile(r"(DEBUG|INFO|WARN|ERROR)[^a-zA-Z]+(.*)")
pattern = re.compile(r"(\w{3} \d{2} \d{2}:\d{2}:\d{2}).*(DEBUG|INFO|WARN|ERROR)[^a-zA-Z]+(.*)")
# pattern = re.compile(r"\w* -")
# print(pattern.findall("main - INFO * Processing request"))
# print(pattern.findall("Process - INFO -> Running sync-classic in 'normal'"))
# print(pattern.findall("Exception: ERROR: column \"SUBJECT_breakCODE\" does not exist"))
print(pattern.search("Dec 21 16:56:00 preprod3 docker/sync-runner[11146]: Exception: "
                     "ERROR: column \"SUBJECT_breakCODE\" does not exist").groups())
with open("sync.log", 'r') as f:
    logs = SyncLogParser.parse(f)

for log in logs:
    print(log.level)
