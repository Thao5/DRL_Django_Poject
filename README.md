# DRL_Django_Poject

Phần database tạo một schema có tên là drldb có charset là utf8mb4 và collation utf8mb4_unicode dòng cuối
Sang python mở thư mục project bằng IDE chạy python(pycharm) trong menu File chọn Settings -> Projects: -> Python
Interpreter -> Add Interpreter
Sau đó mở terminal cd vào DRLProj bằng cmd rồi nhập lệnh pip install -r requirments.txt
Nếu có database sẵn thì vào MySQL chọn trên thanh menu Server -> Data Import -> chọn Import from Self-Contained File
-> chọn drldb.sql trong thư mục này

Sau các bước trên thì chạy python manage.py runserver trên terminal để chạy server
