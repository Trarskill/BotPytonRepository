from PIL import Image

def image_to_ascii(image_path, new_width=27):
    # Открываем изображение
    img = Image.open(image_path)

    # Вычисляем соотношение сторон
    aspect_ratio = img.height / img.width
    new_height = int(new_width * aspect_ratio * 0.55)

    # Изменяем размер изображения
    img = img.resize((new_width, new_height))

    # Конвертируем изображение в градации серого
    img = img.convert('L')

    # Получаем пиксели изображения
    pixels = img.getdata()

    # Символы ASCII для градаций серого
    # chars = "@%#*+=-:. "
    # chars = "⠀⡀⠄⠂⠁⠤⠆⠢⠒⠅⢈⠊⠑⠃⠉⠖⠦⠴⠙⠋⠓⠚⠍⠥⠎⠕⠇⢰⠶⠛⠏⠟⠧⠝⠞⠭⢸⡇⣶⠿⣾⣷⢿⡿⣿"
    chars = "⠿⣶⠶⠛⠁⠐⠐⠂⠐⡀⠀"

    # Преобразуем пиксели в ASCII-символы
    ascii_str = ''.join((chars[pixel // 32] for pixel in pixels))

    # Формируем ASCII-строку для вывода
    ascii_str_len = len(ascii_str)
    img_ascii = "\n".join([ascii_str[index: index + new_width] for index in range(0, ascii_str_len, new_width)])

    return img_ascii