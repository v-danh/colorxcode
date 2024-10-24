# import json
# from rich.console import Console
#
# console = Console()
#
# # tạo một từ điển chứa các mã màu
# colors = {
#     "red": {
#         "RGB": [255, 0, 0],
#         "HEX": "#FF0000",
#         "CMYK": [0, 100, 100, 0]
#     },
#     "green": {
#         "RGB": [0, 255, 0],
#         "HEX": "#00FF00",
#         "CMYK": [100, 0, 100, 0]
#     },
#     "blue": {
#         "RGB": [0, 0, 255],
#         "HEX": "#0000FF",
#         "CMYK": [100, 100, 0, 0]
#     },
#     "cyan": {
#         "RGB": [0, 255, 255],
#         "HEX": "#00FFFF",
#         "CMYK": [100, 0, 0, 0]
#     },
#     "yellow": {
#         "RGB": [255, 255, 0],
#         "HEX": "#FFFF00",
#         "CMYK": [0, 0, 100, 0]
#     },
#     "orange": {
#         "RGB": [255, 165, 0],
#         "HEX": "#FFA500",
#         "CMYK": [0, 35, 100, 0]
#     },
#     "black": {
#         "RGB": [0, 0, 0],
#         "HEX": "#000000",
#         "CMYK": [0, 0, 0, 100]
#     },
#     "pink": {
#         "RGB": [255, 192, 203],
#         "HEX": "#FFC0CB",
#         "CMYK": [0, 25, 20, 0]
#     },
#     "purple": {
#         "RGB": [128, 0, 128],
#         "HEX": "#800080",
#         "CMYK": [0, 100, 0, 50]
#     },
#     "white": {
#         "RGB": [255, 255, 255],
#         "HEX": "#FFFFFF",
#         "CMYK": [0, 0, 0, 0]
#     },
#     "grey": {
#         "RGB": [128, 128, 128],
#         "HEX": "#808080",
#         "CMYK": [0, 0, 0, 50]
#     },
#     "brown": {
#         "RGB": [165, 42, 42],
#         "HEX": "#A52A2A",
#         "CMYK": [0, 75, 75, 35]
#     }
# }
#
# # lưu trữ từ điển dưới dạng JSON vào tệp tin
# with open("colors.json", "w") as file:
#     json.dump(colors, file, indent=4)
#
# console.log("[bold green]Lưu trữ mã màu thành công vào tệp tin colors.json[/bold green]")
