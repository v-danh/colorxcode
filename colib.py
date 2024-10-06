from colorxcode.convert import ColorLib
from rich.console import Console
import logging

console = Console()
result = ColorLib.Color()

# logger = logging.getLogger(__name__)
# LOG_FMT = '%(asctime)s (%(filename)s:%(lineno)d:%(process)s) | <%(levelname)s> %(message)s'
# logging.basicConfig(level=logging.DEBUG,
#                     format=LOG_FMT, datefmt='%d/%m/%Y %H:%M:%S',
#                     handlers=[logging.StreamHandler()])

console.log(f"Mã RGB của màu đỏ : {result.rgb('red')}")
console.log(f"Mã RGB của màu xanh lá : {result.rgb('green')}")
console.log(f"Mã RGB của màu xanh dương : {result.rgb('blue')}")
console.log(f"Mã RGB của màu vàng : {result.rgb('yellow')}")