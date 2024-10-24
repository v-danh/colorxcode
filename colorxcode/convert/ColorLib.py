import builtins
import inspect
import logging
import json
from colorama import init, Fore, Style
from pathlib import Path
from typing import Optional, Union

from colorxcode.convert.logging_config import setup_logging


init(autoreset=True)

SUCCESS_COLOR = Fore.GREEN
INFO_COLOR    = Fore.CYAN
WARNING_COLOR = Fore.YELLOW
ERROR_COLOR   = Fore.RED
RESET         = Style.RESET_ALL

logger = setup_logging()

color_path = Path(__file__).resolve().parent.parent.parent / "colors.json"
class Color:
    color_data: dict[str, dict[str, Union[list[int], str]]] = {}
    _data_loaded: bool = False # cờ để theo dõi việc nạp dữ liệu
    
    @staticmethod
    def _ensure_data_loaded() -> None:
        """Đảm bảo rằng dữ liệu màu đã được nạp trước khi truy vấn."""
        if not Color._data_loaded:
            Color.load_data(color_path)

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
                logger.warning(f"Tệp tin {INFO_COLOR}{json_file.name}{RESET} không tồn tại !")
                return False
            
            with open(json_file, "r", encoding="utf-8") as file:
                Color.color_data = json.load(file)
                Color._data_loaded = True  # đánh dấu là dữ liệu đã được nạp
                logger.info(f"Dữ liệu màu đã được tải từ {INFO_COLOR}{json_file.name}{RESET} thành công.")
                return True
            
        except Exception as e:
            logger.error(f"Lỗi khi tải dữ liệu: {ERROR_COLOR}{e}")
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


def print(*args, **kwargs) -> None:
    """
    Ghi lại thông điệp của `print` bằng `logger`
    """
    message = " ".join(str(arg) for arg in args)

    # Lấy tên hàm gọi `print` bằng cách sử dụng inspect
    caller = inspect.stack()[1].function

    log_level = logging.INFO
    # Gán cấp độ log dựa trên tên hàm
    if caller.startswith("debug_"):
        log_level = logging.DEBUG
    if caller.startswith("warning_"):
        log_level = logging.WARNING
    if caller.startswith("error_"):
        log_level = logging.ERROR
    if caller.startswith("critical_"):
        log_level = logging.CRITICAL

    # Ghi log với cấp độ đã xác định
    logger.log(log_level, message)

# Ghi đè print() mặc định trong toàn bộ chương trình
builtins.print = print


if __name__ == '__main__':

    # tải dữ liệu từ tệp tin
    data = Color.load_data(color_path)
    # kiểm tra nếu việc tải dữ liệu màu thành công
    if data:
        # lấy mã RGB của màu "red"
        result = Color.rgb("red")
        if result:
            logger.info(f"Mã RGB của màu đỏ : {result}")
        else:
            logger.warning("Màu không tồn tại.")
    else:
        logger.error("Không thể tải dữ liệu màu.")
