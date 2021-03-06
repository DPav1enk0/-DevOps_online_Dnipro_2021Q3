# Задание 2.1
### Часть 1. Гипервизоры
  + Версия **Hyper-V Server** подойдет тем, кто не заинтересован в системе аппаратной виртуализации. Эта версия бесплатна и не имеет процедурных ограничений. Однако, у нее есть и свои особенности:
1. Все виртуальные машины, работающие под управлением Windows нужно лицензировать.
2. Решение поддерживает работу с удаленной консолью, но не имеет графического интерфейса.
3. Разработчик не поддерживает эту версию, но для нее доступны обновления.

+ У **VMware** есть и бесплатные решения ESXi Free и VMware Free vSphere Hypervisor. Первое требует регистрации и доступно в режиме пробной бесплатной версии без ограничений функциональности в течение 60 дней, по истечении которых нужно будет или мириться с ограничениями бесплатной версии, или приобретать полноценную.

Бесплатное решение VMware Free vSphere Hypervisor, хоть и не предлагает ограничений для хоста по памяти и процессорам, обладает целым рядом других ограничений.

1. API доступны только для чтения.
2. Виртуальная машина не может иметь больше 8 виртуальных процессоров.
3. Не поддерживается совместная работа с Veeam для резервного копирования.
4. Невозможно подключение к vCenter Server.
5. Не поддерживаются VM host live migration, VM storage live migration.
6. Нет поддержки высокой доступности.
    
  Приведем краткое тезисное сравнение этих двух решений:
    
+ Самым дорогим решением сегодня является VMware, Hyper-V дешевле.
+ При расчете стоимости системы виртуализации кроме самого гипервизора нужно учесть и стоимость лицензий ПО, устанавливаемого на виртуальные машины. С этой позиции Hyper-V поможет дополнительно сэкономить по сравнению с VMware.
+ В гиперконвергентных решениях Hyper-V существенно дешевле.
+ В решении VMware реализован механизм обеспечения отказоустойчивости, в решении Microsoft пока нет.
+ У VMware лучше реализация VDI, но в случае с Hyper-V организация VDI обойдется дешевле.
+ Решение Hyper-V менее требовательно к аппаратной части.
+ В случае использования Hyper-V организация хранилища обойдется дешевле, чем VMware.
+ В VMware есть специальные средства для балансировки нагрузок между ресурсами хостов, в Hyper-V таких средств нет.
+ Благодаря System Center Virtual Machine Manager в Hyper-V есть возможность не просто реализовывать проекты простой серверной виртуализации, но и создавать частные облака.
### Часть 2. Таблица проверки сети при разных настройках виртуальной машины

| Type        | VM⟷VM     | VM➞Host    | Host➞VM      | VM ➞ Lan   | Lan ➞ VM       |
| ------------|:-----------:|:-----------:|:------------:|:-----------:|:---------------:|
| NAT         | есть доступ | есть доступ |порт 8022(ssh)| есть доступ | порт 8080(http) |
| NAT NETWORK | есть доступ | есть доступ |порт 8022(ssh)| есть доступ | порт 8080(http) |
| Bridged     | есть доступ | есть доступ | есть доступ  | есть доступ | есть доступ     |
| Internal Net| есть доступ | нет доступа | нет доступа  | нет доступа | нет доступа     |
|  Host only  | есть доступ | есть доступ | есть доступ  | нет доступа | нет доступа     |
  1. **Nat** 
 > 1 Этот сетевой режим включен для виртуального сетевого адаптера по умолчанию. Гостевая операционная система на виртуальной машине может получить доступ к узлам в физической локальной сети (LAN) с помощью устройства виртуального NAT (трансляции сетевых адресов). Внешние сети, включая Интернет, доступны из гостевой ОС. Гостевая машина недоступна с хост-машины или с других машин в сети, когда для сети VirtualBox используется режим NAT. Этого сетевого режима по умолчанию достаточно для пользователей, которые хотят использовать виртуальную машину только для доступа в Интернет.
  3. **Nat net**
 > 2 Этот режим аналогичен режиму NAT, который вы используете для настройки маршрутизатора. Если вы используете сетевой режим NAT для нескольких виртуальных машин, они могут связываться друг с другом через сеть. Виртуальные машины могут получить доступ к другим хостам в физической сети и могут получить доступ к внешним сетям, включая Интернет. Любая машина из внешних сетей, а также из физической сети, к которой подключен хост-компьютер, не может получить доступ к виртуальным машинам, настроенным для использования сетевого режима NAT (аналогично тому, как вы настраиваете маршрутизатор для доступа в Интернет из вашей домашней сети). Вы не можете получить доступ к гостевому компьютеру с главного компьютера при использовании сетевого режима NAT (если вы не настраиваете переадресацию портов в глобальных сетевых настройках VirtualBox).
  5. **Bridged**
 > 3 Этот режим используется для подключения виртуального сетевого адаптера виртуальной машины к физической сети, к которой подключен физический сетевой адаптер хост-машины VirtualBox. Виртуальный сетевой адаптер виртуальной машины использует сетевой интерфейс хоста для сетевого подключения. Проще говоря, сетевые пакеты отправляются и принимаются напрямую от / к виртуальному сетевому адаптеру без дополнительной маршрутизации. VirtualBox использует специальный драйвер сетевого фильтра для режима мостовой сети, чтобы фильтровать данные с физического сетевого адаптера хоста.
  7. **Internal Network**
 > 4 Виртуальные машины, адаптеры которых настроены для работы в режиме внутренней сети VirtualBox, подключены к изолированной виртуальной сети. Виртуальные машины, подключенные к этой сети, могут взаимодействовать друг с другом, но они не могут взаимодействовать с хост-машиной VirtualBox или с любыми другими хостами в физической сети или во внешних сетях. К виртуальным машинам, подключенным к внутренней сети, нельзя получить доступ с хоста или любых других устройств. Внутреннюю сеть VirtualBox можно использовать для моделирования реальных сетей.
  9. **Host only**
 > 5 Этот сетевой режим используется для связи между хостом и гостями. Виртуальная машина может взаимодействовать с другими виртуальными машинами, подключенными к сети только для хоста, и с хост-машиной. Хост-компьютер VirtualBox может получить доступ ко всем виртуальным машинам, подключенным к сети только для хоста.
---
[Команды для Vagrant](/m2/vagrantinfo.txt)

[Cкриншоты](/m2/screenshots.pdf)



