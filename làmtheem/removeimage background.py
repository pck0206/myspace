from rembg import remove
from PIL import Image
import io

input_path = r"c:\học python\pythonProject1\khoa\làmtheem\pic.jpg"
output_path = r"c:\học python\pythonProject1\khoa\làmtheem\pic.png"

# Mở ảnh dưới dạng byte
with open(input_path, "rb") as input_file:
    input_image_bytes = input_file.read()

# Loại bỏ nền
output_image_bytes = remove(input_image_bytes)

# Chuyển byte kết quả thành đối tượng PIL.Image
output_image = Image.open(io.BytesIO(output_image_bytes))

# Lưu kết quả
output_image.save(output_path)

# Mở ảnh kết quả
output_image.show()