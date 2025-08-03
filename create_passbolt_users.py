import csv
import subprocess
import os
from datetime import datetime

# Input and output
CSV_FILE = 'users.csv'

# Create timestamp
timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
FILENAME = f'passbolt_registration_links_{timestamp}.txt'
OUTPUT_DIR = '/opt/passbolt/passbolt_links/passbolt_registration_links'
OUTPUT_PATH = os.path.join(OUTPUT_DIR, FILENAME)

# Docker command template
CMD_TEMPLATE = '''docker compose -f docker-compose-ce.yaml exec passbolt su -m -c \
"/usr/share/php/passbolt/bin/cake passbolt register_user \
-u {email} -f {first_name} -l {last_name} -r admin" -s /bin/sh www-data
'''

def register_users():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(CSV_FILE, newline='') as csvfile, open(OUTPUT_PATH, 'w') as outfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row.get('Username')
            first_name = row.get('FirstName')
            last_name = row.get('LastName')

            if not all([email, first_name, last_name]):
                print(f"❌ Skipping invalid row: {row}")
                continue

            print(f"🚀 Registering {email}...")
            command = CMD_TEMPLATE.format(email=email, first_name=first_name, last_name=last_name)

            try:
                result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                output = result.stdout

                # Extract registration link
                for line in output.splitlines():
                    if line.startswith("https://"):
                        outfile.write(f"{email}\n{line}\n{'-' * 30}\n")
                        print(f"✅ Registered: {email}")
                        break
                else:
                    print(f"⚠️ No URL found in output for {email}")

            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to register {email}: {e.stderr}")
                outfile.write(f"{email}\nERROR: Registration failed.\n{'-' * 30}\n")

    print(f"\n📁 All registration links saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    register_users()
