import json
from rich.console import Console
import colorxcode
print(colorxcode.__version__)

console = Console()

# in ra đường dẫn hiện tại để kiểm tra
# print(f"Current directory: {Path.cwd()}")
# print(f"Checking if 'colors.json' exists: {Path('colors.json').exists()}")

# đọc dữ liệu từ file colors.json
with open("colors.json", "r") as file:
    color_data = json.load(file)

# truy cập mã màu
def get_color_info(color_name: str) -> list | str:
    color_info = color_data.get(color_name.lower())
    if color_info:
        return f"Color: {color_name.capitalize()}\nRGB: {color_info['RGB']}\nHEX: {color_info['HEX']}\nCMYK: {color_info['CMYK']}"
    else:
        return f"Color '{color_name}' not found."

# ví dụ: lấy mã màu của "red"
console.log(get_color_info("red"),'\n')
console.log(get_color_info("green"),'\n')
console.log(get_color_info("blue"))