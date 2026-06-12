import os
os.makedirs('test', exist_ok=True)
with open('test/README.md', 'w') as f:
    f.write('''This is a test file''')
# This script creates and writes a simple test file
import os
os.makedirs('test', exist_ok=True)
with open('test/README.md', 'w') as f:
    f.write('## Example Content\nThis is a test file')


# local config only
import os
os.makedirs('test', exist_ok=True)
with open('test/README.md', 'w') as f:
    f.write('''This is a test file''')

# local config only
import os
os.makedirs('test', exist_ok=True)
with open('test/README.md', 'a') as f:
    f.write('## Example Content\nThis is a test file')

# local config only
import os
os.makedirs('test', exist_ok=True)
with open('test/README.md', 'w') as f:
    f.write('''This is a test file''')

# local config only
import os
os.makedirs('test', exist_ok=True)
with open('test/README.md', 'r') as f:
    print(f.read())```

# local config only