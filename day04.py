import re

with open("input.txt") as file_content:
    sections = file_content.read().splitlines()

complete_overlap = 0
partial_overlap = 0
for section in sections:
    section1_min, section1_max, section2_min, section2_max, = map(int, re.findall(r'\d+', section))
    if (section1_min >= section2_min and section1_max <= section2_max) or \
            (section2_min >= section1_min and section2_max <= section1_max):
        complete_overlap += 1
    if section2_min <= section1_min <= section2_max or \
            section2_min <= section1_max <= section2_max or \
            section1_min <= section2_min <= section1_max or \
            section1_min <= section2_max <= section1_max:
        partial_overlap += 1
print(complete_overlap)
print(partial_overlap)
