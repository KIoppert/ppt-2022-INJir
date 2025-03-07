# Шаблон репозитория
## Для выполнения задач финала по Передовым производственным технологиям Национальной технологической олимпиады
Привет! Поздравляем, ты стал финалистом нашего профиля. Самое интересное все еще впереди! Пришло время решать задачи заключительного этапа!
 
## Модули
В данных репозиториях будут собираться решения задач из модуля Высокоуровневое программирование.
 
Подробнее про постановку задач вы можете посмотреть в Описание задач заключительного этапа  ППТ 2021/22.
 
 
## Вступление
Перед началом выполнения задач настоятельно рекомендуем прочесть:
- Расширенные правила проведения финала;
- Описание задач заключительного этапа  ППТ 2021/22
 
В этих документах собрана информация про задачи, методы оценивания, а также правила участия в финале. Вы должны их знать.
 
> Помните: Незнание закона не является оправданием!
 
## Перед началом работы
### Fork репозитория
Для начала работы сделайте `fork` этого репозитория. Важно! Ваш репозиторий должен быть `private`, чтобы другие команды не могли получить доступ к вашему решению! В репозиторий разрешено добавлять только организаторов и участников вашей команды.
 
Обязательно в качестве `Collaborator` нужно пригласить в репозиторий следующие аккаунты:
- Andrianov-Artemii
- alexandraDem
- SuslikChan
 
Репозиторий должен иметь название `ppt-2022-<название-команды-латиницей>`. Так, например, команда `Покр-н inds` должна создать репозиторий `ppt-2022-pokr-n-inds`.
 
 
### Ветки и директории
Уже сейчас в вашем репозитории есть две ветки:
- master - основная ветка
- checked - ветка для принятых решений
 
Также в репозитории есть шесть папок:
- ppt-task-0
- ppt-task-1
- ppt-task-2
- ppt-task-3
- ppt-task-4
- ppt-task-5
 
Каждая папка соответствует одной из предложенных задач.
 
Также в корневой папке есть `docker-compose.yml`. Этот файл мы в дальнейшем используем для ручной проверки ваших решений, его также не стоит изменять или редактировать, это может привести к тому, что ваше решение у нас не запустится.
 
> Не стоит менять структуру проекта, удалять или добавлять что-то вне папок с решениями. Структура создана для оптимизации вашей и нашей работы!
 
### Pull request'ы
Для того, чтобы ваше решение было отправлено на проверку вам нужно сделать `pull request` из ветки `master` в ветку `checked`. При открытии запроса на проверку укажите в названии задание (например, если это нулевое задание - укажите в названии `ppt-task-0`). После того, как вы откроете реквест - нам придет уведомление о том, что вы готовы к проверке и мы придем к вам в порядке очереди.
 
Если в ожидании проверки вы обнаружили, что ваше решение неверно и хотите сняться с проверки - просто закройте `pull request` кнопкой `Close`.
 
Если после проверки у вас остались вопросы - вы можете задать их в комментариях в `pull request`, отметив организатора, который проверял ваше решение.
 
> Важно! Не делайте `Merge pull request` сами. В таком случае ваше решение не будет проверено! Оставьте право принимать решение и выставлять баллы организаторам. Если ваше решение будет правильным - мы оценим его на наивысший балл!

### Issues
Если вы хотите задать вопросы по условию задач - вы можете сделать это в разделе `Issues` головного репозитория (`ppt-template-2022`). Так ваш вопрос и наш ответ увидят все команды. Это честно и позволяет поставить все команды в равное положение.
 
> Важно! Запрещается отправлять в `issue` элементы решений. Если вы хотите оспорить решение или задать по нему вопросы после проверки - используйте комментарии в `pull request`.

## Запуск решения
Запустить решение во время разработки можно двумя способами:
- Запустить его, как обычную программу через `python main.py`
- Запустить его в виде контейнера. Для этого стоит выполнить следующие команды:
```sh
    # Сборка контейнера
    $ docker build -t solution . 
    # Запуск контейнера и установка связи между хостом и контейнером на 80 порту
    $ docker run -p 80:80/udp --rm solution 
```
Для этого способа также потребуется наличие установленного на компьютере [Docker](https://www.docker.com/products/docker-desktop/).
 
> Оба способа запуска решения при разработке будут корректными, однако стоит учесть, что при проверке мы используем именно второй способ и его вариации! Для запуска задач с UI стоит использовать первый способ, так как иначе необъодимо будет настроить запуск GUI из контейнера.

## Библиотеки
Если ваше решение требует использования дополнительных библиотек - их необходимо указать в файле requirements.txt. Также в Dockerfile нужно добавить строчку
```Dockerfile
    RUN pip3 install -r requirements.txt
```

## Проверка решений
Все решения проходят автоматическую и ручную проверку.
 
### Автоматическая проверка
Автоматическая проверка выполняется на базе GitHub Actions. Данная проверка является первичной и позволяет проверить, что решение правильно упаковано и в нем присутствуют все необходимые файлы.
 
** GitHub Actions дает доступ к своим тестами только на 2000 минут в месяц (Примерно 33 часа). Учитывайте это при распределении рабочего времени. В случае, если вы истратили все минуты - сообщите об этом организаторам через раздел `Issues`. **
 
После прохождения тестов, нам автоматически придет уведомление о том, что вы готовы к проверке.
 
> Важно! Не пытайтесь вмешиваться в работу автоматической системы проверки или попытаться изменить алгоритм самой проверки. Это может быть расценено, как попытка фальсификации при сдачи решения.
 
### Что делать, если решение не прошло автоматические тесты
Если при попытке отправить решение на проверку у вас упали тесты, то не стоит переживать. Просто исправьте недочеты, основываясь на логах тестов и сделайте `push` в ветку `master`. Изменения автоматически подтянутся в ваше решение. После, перезапустите проверку решения двумя способами:
- Закройте и откройте заново `pull request`;
- Зайдите в раздел `Actions`, выберите упавший `workflow` и нажмите на кнопку `Re-run all jobs`.
 
### Ручная проверка
При ручной проверке мы выкачиваем ваше решение в виде исходных файлов для сборки docker контейнера. После происходит сборка решения и его последующее тестирование.
 
Ручная проверка проводится в режиме живой очереди. Проверяющий присоединится к вам в Discord чате при проверке, чтобы вы знали что именно происходит во время проверки вашего решения на площадке.
 
### Что делать, если решение не принято
Если после проверки организаторы закрыли ваш `pull request` - это значит, что решение оценено в ноль баллов. Это может произойти, если решение нарушает Технику Безопасности или работает неправильно. В таком случае внесите исправления и сделайте `push` в ветку `master`. А после переоткройте `pull request`.


### Что делать, если решение принято
Если после принятия решения у вас пропала ветка мастер - сделайте ее заново от ветки 'checked'. Нейминг ветки при проверки тестов (кроме `checked`) не учитывается.

Советуем создавать ветку с названием вида `ppt-task-N`.