# Key-M_test_task

СТВОРИТИ КЛАС З МЕТОДОМ, ЯКИЙ БУДЕ СТВОРЮВАТИ НОТИФІКАЦІЇ:
1. Клас який буде створювати нотифікації notification template - скрипт - функція, викликом якої створюються нотифікації
2. Параметри для кожноъ нотифыкацыъ беруться з user_norification_option
3. user_notification_setting - хоче чи ні юзер бачити нотифікацію
system notification type = 1 / push notification type = 2
user_notification - status = чи нотифікація прочитана?
4. Коли юзер прочитав нотифікацію - змінити status - створити відповідний PUT method
5. GET method - зі списком нотифікації, в т.ч. фільтрацію по статусу (прочитан ,чи ні), по notifiction_type notification_category
