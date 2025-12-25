import qrcode
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python qr_cli.py <text_or_url>")
        return

    data = sys.argv[1]
    img = qrcode.make(data)

    filename = "qr_code.png"
    img.save(filename)

    print("\n✅ QR Code Generated")
    print(f"📁 Saved as: {filename}")
    print(f"🔗 Data: {data}\n")

if __name__ == "__main__":
    main()
# --------------------------------------------------
# Built by Kuroi Hub
# Author: Independent Developer
# License: MIT (Commercial Use Allowed, No Resale)
# https://kuroihub.netlify.app
# --------------------------------------------------
