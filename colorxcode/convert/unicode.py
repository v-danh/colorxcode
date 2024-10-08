from rich.console import Console
from rich.text import Text
from typing import Optional
from colorxcode.convert import ColorLib

console = Console()
r = ColorLib.Color()

def colored_unicode(color_name: str) -> Optional[str]:
    """
    Biểu diễn mã màu theo ký tự Unicode với màu tương ứng.
    Sử dụng thư viện `rich` để hiển thị màu trực tiếp trên dòng lệnh.
    """
    rgb = r.rgb(color_name)
    
    if rgb:
        # Chuyển đổi RGB sang định dạng HEX
        hex_color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        
        # Tạo một kí tự có màu tương ứng
        colored_symbol = Text("■", style=f"bold {hex_color}")  # dùng kí hiệu hình vuông "■"
        
        # In ký tự màu trên console
        console.log(colored_symbol)
        
        return f"Unicode color symbol: {hex_color}"
    else:
        return None

colored_unicode("red")
colored_unicode("green")
colored_unicode("blue")
colored_unicode("")
