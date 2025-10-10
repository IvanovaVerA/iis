## О чем проект

Проект посвящен решению задачи предсказания классификации цен на мобильные устройства. Ссылка на исходную выборку данных: https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification?resource=download

## Запуск

Для запуска проекта необходимо выполнить команды:
```
git clone git@github.com:IvanovaVerA/iis.git
```
или:
```
git clone https://github.com/IvanovaVerA/iis.git
```
переход в папку:
```
cd IIS
```
установка окружения:
```
python -m venv .venv -
```
активация окружения:
```
source .venv/bin/activate
```
установка зависимостей:
```
python -m pip install -r requirements.txt 
```

## Исследование данных

Находится в ./eda/eda.ipynb. Основные результаты:

В ходе исследования были проведены действия:

   - Удалены записи с нулевыми значениями для признаков battery_power, clock_speed, int_memory, m_dep

   - Установлены минимальные значения для размера мобильного устройства: mobile_wt, px_height, px_width

   - Удалены строки, у которых ширина (sc_w) больше высоты (sc_h)



В ходе анализа были выявлены следующие закономерности:

   - Наибольшая корреляция с целевой переменной (price_range) наблюдается у ram (0.92) (см. графики ./eda/CorrelationHeatmap.png и ./eda/ram_vs_price.png)

   - Так же значимыми признаками являются px_height и px_width и была создана новая переменная total_pixels = px_height * px_width (см. график ./eda/new_features.png)

   - имеется положительная линейная зависимость между вуысотой и шириной экрана мобильного устройства