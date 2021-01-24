# traceroute_python3
Version: 2.0

Автор: Полтораднев Кирилл
Дата: 24.01.2021

## Описание
Утилита traceroute предназначенная для определения маршрутов следования данных в сетях TCP/IP. Traceroute может использовать разные протоколы передачи данных в зависимости от операционной системы устройства. Такими протоколами могут быть UDP или ICMP.


## Состав
* Файл запуска утилиты: `traceroute.py`
* Модули: `/modules`
* Логика: `/modules/traceroute`
* Пакеты IPv4: `/ipv4packet`
* Тесты: `/tests`

### Управление
`python3  [-h] [-f FIRST_HOP] [-I] [-m MAX_HOPS] [-M METHOD] [-p PORT] [-q PACKET_NUMBER] [-w TIMEOUT] destination`

Для работы утилита использует параметры:

* `-h`, `--help` отобразить сообщение help
* `-f FIRST_HOP`, `--first-hop FIRST_HOP` установить начальный параметер TTL (time to live)0 (по умолчанию: 1)
* `-I`, `--icmp` использовать протокол ICMP для пинга серверов
* `-m MAX_HOPS`, `--max-hop MAX_HOPS` установить максимальное кол-во промежуточных серверов
* `-M METHOD`, `--method METHOD` используйте METHOD ("icmp" или "udp") для выборо протокола формирования запросов traceroute
* `-p PORT`, `--port PORT` используйте PORT в качестве порта назначения (по умолчанию: 33434)
* `-q PACKET_NUMBER`, `--tries PACKET_NUMBER` укажите PACKE_NUMBER в качестве кол-ва отправляемых пакетов на один сервер (по умолчанию: 3)
* `-w TIMEOUT`, `--wait TIMEOUT` укажите TIMEOUT в качестве времени ожидания ответа от сервера (по умолчанию: 3)

## Подробности реализации
Модули, отвечающие за логику краулера расположены в пакете modules. 
* `modules.ProtocolManager` - класс, формирующий пакет запроса по выбранному протоколу
* `modules.SocketManager`- класс, реализующий обрабоку отпраления и получения данных через сокеты
* `modules.TerminalParser`- класс, реализующий argparser для обработки терминальной команды
* `modules.TerminalPrinter` - класс, реализующий методы для печати результатов работы утилиты
* `modules.traceroute.TracerouteInfo` - структура данных для хранения параметров запуска утилиты
* `modules.traceroute.Traceroute` - класс, реализующий логику работы утилиты
* `ipv4packet.IP.IPHeader` - структура данных для формирования IP заголовка
* `ipv4packet.IP.IP` - класс-обертка над `IPHeader`
* `ipv4packet.UDP.UDPHeader` - структура данных для формирования UDP сообщения
* `ipv4packet.UDP.UDP` - класс-обертка над `UDPHeader`
* `ipv4packet.ICMP.ICMPHeader` - структура данных для формирования ICMP сообщения
* `ipv4packet.ICMP.ICMP` - класс-обертка над `ICMPHeader`
