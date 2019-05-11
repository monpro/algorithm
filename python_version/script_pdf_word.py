from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

resource_manager = PDFResourceManager()
return_str = io.StringIO()	
lap_params = LAParams()

device = TextConverter(resource_manager, return_str, laparams=lap_params)
process_pdf(resource_manager, device, file)  # file是使用open方法打开的PDF文件句柄
device.close()

# 此处content就是转换为文字的PDF内容
content = return_str.getvalue()
