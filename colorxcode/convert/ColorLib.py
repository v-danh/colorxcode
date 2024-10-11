import json
from pathlib import Path
from rich.console import Console
from typing import Optional, Union

console = Console()

class Color:
    color_data: dict[str, dict[str, Union[list[int], str]]] = {}
    _data_loaded: bool = False # cờ để theo dõi việc nạp dữ liệu
    
    @staticmethod
    def _ensure_data_loaded() -> None:
        """Đảm bảo rằng dữ liệu màu đã được nạp trước khi truy vấn."""
        if not Color._data_loaded:
            Color.load_data(Path("colors.json"))

    # tải dữ liệu từ tệp JSON
    @staticmethod
    def load_data(json_file: Path) -> bool:
        """
        Tải dữ liệu màu từ tệp JSON vào biến `color_data`.
        
        Args:
            json_file (Path) : đường dẫn đến tệp `JSON`.

        Returns:
            bool : trả về `True` nếu thành công, ngược lại là `False`.
        """
        try:
            if not json_file.exists():
                console.log(f"[bold red]Tệp tin '{json_file}' không tồn tại.[/bold red]")
                return False
            
            with open(json_file, "r", encoding="utf-8") as file:
                Color.color_data = json.load(file)
                Color._data_loaded = True  # đánh dấu là dữ liệu đã được nạp
                console.log(f"[bold green]Dữ liệu màu đã được tải từ {json_file} thành công ![/bold green]")
                return True
            
        except Exception as e:
            console.log(f"[bold red]Lỗi khi tải dữ liệu: {e}[/bold red]")
            return False

    @staticmethod
    def get_color(color_name: str) -> Optional[dict[str, Union[list[int], str]]]:
        """
        Lấy thông tin màu theo tên màu.\n
        Trả về từ điển chứa các mã màu hoặc `None` nếu màu không tồn tại.
        """
        Color._ensure_data_loaded()  # đảm bảo dữ liệu đã được nạp trước khi truy vấn
        return Color.color_data.get(color_name.casefold())
    
    @staticmethod
    def get_color_format(color_name: str, format_type: str) -> Optional[Union[list[int], str]]:
        """
        Lấy mã màu theo định dạng (RGB, HEX, CMYK).
        """
        color_info = Color.get_color(color_name)
        if color_info:
            return color_info.get(format_type.upper(), None)
        return None
    
    # các hàm để lấy mã màu theo định dạng cụ thể
    @staticmethod
    def rgb(color_name: str) -> Optional[list[int]]:
        """
        Convert into RGB code
        """
        return Color.get_color_format(color_name, "RGB")
    
    @staticmethod
    def hex(color_name: str) -> Optional[str]:
        """
        Convert into HEX code
        """
        return Color.get_color_format(color_name, "HEX")
    
    @staticmethod
    def cmyk(color_name: str) -> Optional[list[int]]:
        """
        Convert into CMYK code
        """
        return Color.get_color_format(color_name, "CMYK")

if __name__ == '__main__':
    file_path = Path("colors.json")
    # tải dữ liệu từ tệp tin
    data = Color.load_data(file_path)
    # kiểm tra nếu việc tải dữ liệu màu thành công
    if data:
        # lấy mã RGB của màu "red"
        result = Color.rgb("red")
        if result:
            console.log(f"[bold blue]Mã RGB của màu đỏ[/bold blue] : {result}")
        else:
            console.log("[bold red]Màu không tồn tại.[/bold red]")
    else:
        console.log("[bold red]Không thể tải dữ liệu màu.[/bold red]")
