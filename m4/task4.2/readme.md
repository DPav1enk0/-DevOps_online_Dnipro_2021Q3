# Networking Fundamentals #


1. Номера VLAN (VLAN ID)
Номера VLAN (VLAN ID) могут быть в диапазоне от 1 до 4094:

1 - 1005 базовый диапазон (normal-range)
1002 - 1005 зарезервированы для Token Ring и FDDI VLAN
1006 - 4094 расширенный диапазон (extended-range)
 

 *Параметры VLAN*
При создании или изменении VLAN можно задать следующие параметры:

* VLAN ID - Номер VLAN
* VLAN name (name) - Имя VLAN
* VLAN type (media) - Тип VLAN (Ethernet, Fiber Distributed Data Interface [FDDI], FDDI network entity title [NET], TrBRF, или TrCRF, Token Ring, Token Ring-Net)
* VLAN state (state) - Состояние VLAN (active или suspended)
* VLAN MTU (mtu) - Максимальный размер блока данных, который может быть передан на канальном уровне
* SAID (said) - Security Association Identifier - идентификатор ассоциации безопасности (стандарт IEEE 802.10)
* Remote SPAN (remote-span) - Создание VLAN для удаленного мониторинга трафика (В дальнейшем в такой VLAN можно зеркалировать трафик с какого-нибудь порта, и передать его через транк на другой коммутатор, в котором из этого VLAN трафик отправить на нужный порт с подключенным снифером)
* Bridge identification number для TrBRF VLAN (bridge) - Идентификатор номера моста для функции TrBRF (Token Ring Bridge Relay Function). Цель функции - создание моста из колец.
* Ring number для FDDI и TrCRF VLAN (ring) - Номер кольца для типов VLAN FDDI и TrCRF (Token Ring concentrator relay functions). TrCRF называют кольца, которые включены в мост.
* Parent VLAN number для TrCRF VLAN (parent) - Номер родительского VLAN для типа VLAN FDDI или Token Ring
* Spanning Tree Protocol (STP) type для TrCRF VLAN (stp type) - Тип протокола связующего дерева (STP) для VLAN типа TrCRF
* Translational VLAN number 1 (tb-vlan1) - Номер VLAN для первичного преобразования одного типа VLAN в другой
* Translational VLAN number 2 (tb-vlan2) - Номер VLAN для вторичного преобразования одного типа VLAN в другой
 
***
[Настройка VLAN CISCO](https://linkas.ru/articles/vlan-v-cisco/)

[Скриншоты](/m4/task4.2/screenshots.pdf)






