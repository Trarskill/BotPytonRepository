import cv2

def create_pencil_sketch(image_file):
    # Считываем изображение с файла
    img = cv2.imread(image_file)

    # Преобразуем изображение в градации серого
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Инвертируем цвета изображения
    inverted_img = cv2.bitwise_not(gray_img)

    # Применяем размытие с использованием Гауссова фильтра
    blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), sigmaX=0, sigmaY=0)

    # Делим исходное серое изображение на инвертированное и размытое, создавая эффект карандашного рисунка
    pencil_sketch = cv2.divide(gray_img, 255 - blurred_img, scale=256)

    # Сохраняем результат в виде файла "pencil_sketch.png"
    cv2.imwrite("pencil_sketch.png", pencil_sketch)