class SmartPhone: # создаем класс, в данном случае суть про смартфоны
    model = None       #
    year = None        # три переменные которые описыват модель, год, и наличие кнопки
    button = None      #
    def __init__(self, model, year, button):
        self.set_data(model, year , button)

        self.get_data()

    def set_data(self, model, year , button):
        self.model = model
        self.year = year      # создаем функцию сбора данных и превращаем с помощью селф переменные
        self.button = button

    def get_data(self):

        print("Модель устрйства :", self.model,"\nГод выпуска :",self.year, "\nИмеется ли на дисплее кнопка :", self.button, "\n")
        # создали функцию для вывод информации полученной с помощью Get_Data

class Samsung(SmartPhone):
    demo = "Нет"             # создаем подкласс самсунг зависящий от основного и добавляем новый параметр: демоверсия ли

    def __init__(self, model, demo, year, button):
        super(Samsung, self).__init__(model, year, button)  # С помощью super переносим тот unit в этот
        self.demo = demo  # и добавляем новую переменную

    def get_data(self):

        print("Модель устрйства :", self.model, "  Demo: ", self.demo, "\nГод выпуска :",self.year, "\nИмеется ли на дисплее кнопка :", self.button)


class Iphone(SmartPhone):
    pass


class Xioami(SmartPhone):
    Global = None

    def __init__(self, model, Global, year, button):
        super(Xioami, self).__init__(model, year,button)
        self.Global = Global

    def get_data(self):
        print("Модель устрйства :", self.model, "Версия : ",self.Global, "\nГод выпуска :",self.year, "\nИмеется ли на дисплее кнопка :", self.button)
Iphone_11 = SmartPhone("Iphone 11",2019, "Не имеется")

Iphone_8 = SmartPhone("Iphone 8", 2017, "Имеется одна")

Samsung_S22 = Samsung("Samsung S22","Не демо-версия", 2022, "Не имеется")

Xioami_Redmi_Note_11s_5g = Xioami("Xioami Redmi Note 11S 5G", "Global", 2022, "Не имеется")

Iphone_11.get_data()
Iphone_8.get_data()
Samsung_S22.get_data()
Xioami_Redmi_Note_11s_5g.get_data()