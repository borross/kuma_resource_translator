# kuma_resource_translator
Translate cyrillic strings from JSON to English (Авто перевод контента KUMA на английсикий)

# Предварительные настройки
1. Установите пакет для Python `pip install deep_translator`

2. Пропишите несколько общедоступных прокси, например, с ресурса: [geonode](https://geonode.com/free-proxy-list) и добавьте в коде в переменную `proxies_example`

3. Расшифруйте ресурс KUMA с помощью утилиты [Утилита](https://github.com/Morpheme777/kuma_packages_encryption)

4. Укажите полный путь в переменной в коде до расшифрованного ресурса: `file_path`, например, `c:/Users/boris/Downloads/Community-Pack-CorrelationRules_RU_dec.json`

# Запуск
1. Запустите скрипт `kuma_resource_translator.py`

2. Результат запишется в файл `*processed.json`

3. Зашифруйте файл `*processed.json` в ресурс KUMA утилитой из п.3 предварительных настроек
