# Крестики-нолики

### Описание проекта:
* Необходимо разработать консольную игру "Крестики-нолики" для двух игроков с использованием принципов объектно-ориентированного программирования. Игра должна быть выполнена в консольном интерфейсе с возможностью интерактивного ввода от пользователей.

### Цели и задачи:
* Реализовать игру с понятной иерархией классов.
* Использовать ООП-принципы
* Обеспечить корректную обработку игровых ситуаций (победа, ничья, ходы по правилам).

### Пример разбития на классы (можно использовать своё видение):

1. Класс `Game` (Основной класс игры):
* *Атрибуты*:
  * `board`: объект класса Board (игровое поле).
  * `player1`: объект класса Player (первый игрок).
  * `player2`: объект класса Player (второй игрок).
  * `current_player`: игрок, который делает текущий ход.

* *Методы*:
  * `start_game()`: запускает игру, инициализирует игроков и игровое поле.
  * `play_turn()`: выполняет один ход игры (ввод координат хода от игрока и их проверка).
  * `switch_player()`: переключает ход между игроками.
  * `check_winner()`: проверяет наличие победителя или ничьей после каждого хода.
  * `display_result()`: выводит результат игры (победа одного из игроков или ничья)
  * `reset_game()`: перезапускает игру, обнуляет игровое поле и готовит игроков к новой игре.


2. Класс `Board` (Игровое поле):
* *Атрибуты*:
  * grid: двумерный список 3x3, представляющий игровое поле (сначала заполняется пустыми значениями, например, None).

* *Методы*:
  * `display_board()`: выводит игровое поле в консоль с текущим состоянием (крестики и нолики).
  * `make_move(x: int, y: int, symbol: str)`: принимает координаты и символ (X или O), ставит его на указанное место на поле.
  * `is_valid_move(x: int, y: int) -> bool`: проверяет, можно ли поставить крестик или нолик в выбранную клетку.
  * `check_full() -> bool`: проверяет, заполнено ли игровое поле (для определения ничьей).
  * `check_winner(symbol: str) -> bool`: проверяет, есть ли победная комбинация для указанного символа (три одинаковых символа по горизонтали, вертикали или диагонали).


3. Класс `Player` (Игрок):
* *Атрибуты*:
  * `name`: имя игрока.
  * `symbol`: символ, которым играет игрок (X или O).

* *Методы*:
  * `make_move(board: Board)`: запрашивает у игрока ввод координат для своего хода и передаёт их в метод make_move() объекта класса Board.
  * `get_name()`: возвращает имя игрока.
  * `get_symbol()`: возвращает символ игрока (X или O).


4. Класс `HumanPlayer` (Игрок-человек, наследник класса `Player`):
* *Методы*:
  * `make_move(board: Board)`: наследует от класса Player, но реализует ввод координат с клавиатуры. Обрабатывает ошибки (например, некорректный ввод или выбор занятой клетки).


5. Класс `AIPlayer` (Игрок-компьютер, наследник класса `Player`):
* *Методы*:
  * `make_move(board: Board)`: реализует автоматический ход компьютера, выбирая случайную свободную клетку (или реализует более сложную стратегию).
