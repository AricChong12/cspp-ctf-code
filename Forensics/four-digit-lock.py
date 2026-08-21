import zipfile
import zlib

zip_file = "locked.zip"

with zipfile.ZipFile(zip_file) as z:
    filename = z.namelist()[0]

    for i in range(10000):
        pin = f"{i:04d}".encode()

        try:
            z.read(filename, pwd=pin)
            print(f"[+] PIN found: {pin.decode()}")
            z.extractall("extracted", pwd=pin)
            print("[+] Extracted to ./extracted/")
            break
        except (RuntimeError, zipfile.BadZipFile, zlib.error):
            pass