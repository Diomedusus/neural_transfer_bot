# Описание проекта "Neural Transfer Telegram bot"
Телеграмм Бот предоставляет возможность переноса стиля одной картинки на другую. За основу брался алгоритм переноса стился описанный [на сайте библиотеки Pytorch](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html).
# Пример работы
![1-2](https://user-images.githubusercontent.com/91438380/215349380-e753749f-32dd-4399-b127-b62c69069de4.jpg)
![kartina-zvezdnaya-noch-van-goga](https://user-images.githubusercontent.com/91438380/215349401-551d6a8c-7660-4644-96e5-520a1727dfc9.jpg)
![photo_2023-01-29_21-37-38](https://user-images.githubusercontent.com/91438380/215349408-f2165814-bfe1-4706-ba84-a2731ab9bb00.jpg)
# Телеграмм API

Для взаимодействия с ботом можно ознакомиться с принципом работы через команды /help и /start. Далее нужно направить картинку для стиля с подписью style, а затем направить картинку, на которую мы будем переносить стиль, подписав ее перед отправкой как content. Если работает CUDA, то картинки придет ответным письмом в течение минуты.
