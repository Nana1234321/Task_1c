# Task_1c
В данной задаче мы реализовали несколько команд:
1)text - на ввод данных (они могут добавляться при повторном вызове команды)
2)request - запрос
3)write - дописывание
4)end - завершение работы
В данном коде я реализовала дописывание так, чтобы префикс функция и циклы начинали работу не с самого начала для всех введенных слов, а только для подходящих
То есть на каждом этапе request я создавала новый словарь - в котором были только те слова, которые будет использовать команда "Дописать", помимо этого я предусмотрела что сначала может быть введён request -> text -> write
т.е. казалось бы что в новый словарб попала часть слов и все НУЖНЫЕ слова в дописывании рассмотрены не будут, НО это не так, потому что на жто мы делаем проверку в команде text и обновляем новый словарб, чтобы он точно содержал все слова

