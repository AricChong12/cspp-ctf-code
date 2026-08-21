import zipfile
from pathlib import Path

current = Path("nested.zip")

while zipfile.is_zipfile(current):
    output = current.parent / "extracted"
    output.mkdir(exist_ok=True)

    print(f"[+] Extracting: {current}")

    with zipfile.ZipFile(current) as z:
        z.extractall(output)

    # Find the next ZIP
    zips = list(output.rglob("*.zip"))

    if not zips:
        print("[+] No more ZIP files.")
        break

    current = zips[0]

print("\n[+] Files remaining:")
for f in current.parent.rglob("*"):
    if f.is_file():
        print(f)