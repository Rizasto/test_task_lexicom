1) Запуск первого задания осуществляется запуском bash скрипта start.sh, находящегося в каталоге first_task
2) Второе задание представлено в виде кода на Python и SQL-инъекции. Для достаточно быстрого выполнения задачи был выбран алгоритм слияния для сравнения названий файлов. При условии наличия 700 тысяч записей в обоих таблицах, тесты показывают результат в 49 секунд для выполнения задачи. В случае, указанном в ТЗ, результат будет немного быстрее. Данную задачу можно решить и быстрее, используя временные таблицы с полным переносом данных и сравнением по ID или любому другому Primary Key. Т.к. как в задании не было укзаано, можно ли удалять таблицу, пересоздавать ее, или дополнять новыми полями, такими как ID, был выбран алгоритм слияния, чтобы не менять существующие таблицы, а лишь дополнять их.
