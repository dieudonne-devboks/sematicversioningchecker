import re

class VersionNumber:
    def __init__(self, pattern: str):
        self.pattern = re.compile(pattern)
    
    def is_valid(self, s: str) -> bool:
        match = self.pattern.fullmatch(s)
        return match is not None
    
    def get_precedence(self, a: str, b: str, c: str) -> Optional[str]:
        if not self.is_valid(a) or not self.is_valid(b) or not self.is_valid(c):
            return None
        
        a_parts = a.split(".")
        b_parts = b.split(".")
        c_parts = c.split(".")
        
        # Compare minor version numbers
        if a_parts[1] > b_parts[1] and a_parts[1] > c_parts[1]:
            return a
        elif b_parts[1] > a_parts[1] and b_parts[1] > c_parts[1]:
            return b
        elif c_parts[1] > a_parts[1] and c_parts[1] > b_parts[1]:
            return c
        
        # Compare patch version numbers
        if a_parts[2] > b_parts[2] and a_parts[2] > c_parts[2]:
            return a
        elif b_parts[2] > a_parts[2] and b_parts[2] > c_parts[2]:
            return b
        elif c_parts[2] > a_parts[2] and c_parts[2] > b_parts[2]:
            return c
        
        # If all version numbers are equal, return the first one
        return a

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
    
def test_get_precedence():
    vn = VersionNumber(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?:[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")
    
    assert vn.get_precedence("1.0.0", "1.0.1", "1.1.0") == "1.1.0"
    assert vn.get_precedence("1.0.1", "1.1.0", "1.0.0") == "1.1.0"
    assert vn.get_precedence("1.1.0", "1.0.0", "1.0.1") == "1.1.0"
    assert vn.get_precedence("1.1.0", "1.1.0", "1.1.0") == "1.1.0"
    assert vn.get_precedence("1.1.0", "1.1.0", "2.0.0") == "2.0.0"
    assert vn.get_precedence("1.0.0-alpha", "1.0.0", "1.0.0-beta") == "1.0.0"
    assert vn.get_precedence("1.0.0-alpha.1", "1.0.0-alpha.2", "1.0.0") == "1.0.0"
    assert vn.get_precedence("1.0.0-alpha", "1.0.0-beta", "1.0.0-alpha.beta")

    
