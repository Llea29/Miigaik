#!/usr/bin/env python
# coding: utf-8

# Задание 1

# In[2]:


get_ipython().system('pip install Pillow')


# In[5]:


import PIL


# In[15]:


from PIL import Image
file_path = "1png.png"
def process_image(file_path):
    try:
        # Загрузка изображения
        image = Image.open(file_path)
        print(f"Формат изображения: {image.format}")

        # Проверка, является ли формат PNG
        if image.format == "PNG":
            # Конвертация изображения в формат RGBA (если не в этом формате)
            if image.mode != "RGBA":
                image = image.convert("RGBA")
            
            # Проверка на прозрачность и обработка
            data = image.getdata()
            new_data = []
            contains_transparency = False

            for item in data:
                # Если пиксель содержит прозрачность (alpha < 255)
                if item[3] < 255:
                    contains_transparency = True
                    new_data.append((255, 255, 255, 255))  # Заменяем на белый цвет
                else:
                    new_data.append(item)
            
            if contains_transparency:
                print("Прозрачные пиксели найдены. Они заменены белыми.")
                image.putdata(new_data)
            else:
                print("Прозрачные пиксели отсутствуют.")
        else:
            print("Файл не в формате PNG, обработка прозрачности не требуется.")

        # Сохранение обработанного изображения
        output_file = file_path.replace(".", "_processed.")
        image.save(output_file)
        print(f"Изображение сохранено как {output_file}")

    except Exception as e:
        print(f"Произошла ошибка при обработке изображения: {e}")

# Пример использования
# file_path = "example.png"  # Укажите путь к вашему изображению
process_image(file_path)


# Задание 2

# In[18]:


from PIL import Image, ImageFilter

def resize_image(image, new_width, new_height):
    """
    Изменяет размер изображения до указанных ширины и высоты.
    """
    return image.resize((new_width, new_height))

def convert_to_grayscale(image):
    """
    Конвертирует изображение в черно-белое (оттенки серого).
    """
    return image.convert("L")

def apply_gaussian_blur(image, radius):
    """
    Применяет фильтр Гаусса (размытие) с заданным радиусом.
    """
    return image.filter(ImageFilter.GaussianBlur(radius))

def process_image(file_path):
    """
    Основная функция: загружает изображение и применяет все обработки.
    """
    try:
        # Открываем изображение
        image = Image.open(file_path)
        print(f"Оригинальный размер изображения: {image.size}")
        
        # 1. Изменение размера
        resized_image = resize_image(image, new_width=200, new_height=200)
        resized_image.save("resized_image.jpg")
        print("Изменённый размер изображения сохранён как 'resized_image.jpg'")

        # 2. Конвертация в черно-белое
        grayscale_image = convert_to_grayscale(image)
        grayscale_image.save("grayscale_image.jpg")
        print("Черно-белое изображение сохранено как 'grayscale_image.jpg'")

        # 3. Применение размытия Гаусса
        blurred_image = apply_gaussian_blur(image, radius=5)
        blurred_image.save("blurred_image.jpg")
        print("Размытое изображение сохранено как 'blurred_image.jpg'")

    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")

process_image(file_path)


# In[21]:


jupyter nbconvert --to script 7.ipynb


# In[ ]:




