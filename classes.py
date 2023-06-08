class Question:

    def __init__(self, text, level, ranswer):
        self.text = text
        self.level = level
        self.ranswer = ranswer
        self.question = False
        self.user_answer = None
        self.balls = 0

    def __get_points(self) -> None:
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        self.balls = int(self.level) * 10

    def is_correct(self) -> bool:
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        if self.user_answer == self.ranswer:
            return True
        return False

    def build_question(self) -> None:
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        print(f'Вопрос: {self.text}')
        print(f'Сложность: {self.level}/4')

    def build_positive_feedback(self) -> str:
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        self.__get_points()
        return f'Ответ верный, получено {self.balls} баллов'

    def build_negative_feedback(self) -> str:
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f'Ответ неверный, верный ответ {self.ranswer}'


# https://jsonkeeper.com/b/T812
