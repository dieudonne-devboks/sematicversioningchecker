import re

class VersionNumber:
    def __init__(self, pattern):
        self.pattern = re.compile(pattern)
    
    def is_valid(self, s):
        match = self.pattern.fullmatch(s)
        return match is not None

# Create a VersionNumber object
version_number = VersionNumber(r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")

# Test some strings
test_strings = [
    "1.0.0",
    "2.3.4-alpha.1",
    "1.2.3+build.1",
    "invalid",
    "1.2.3-invalid",
]

for s in test_strings:
    result = version_number.is_valid(s)
    print(f"{s}: {result}")
