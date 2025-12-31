import re
import random

# Определяем стоп-слова как глобальную переменную
STOP_WORDS = {
    'и', 'в', 'на', 'с', 'по', 'к', 'у', 'о', 'от', 'до',
    'за', 'из', 'для', 'но', 'а', 'или', 'же', 'бы', 'ли',
    'что', 'это', 'как', 'так', 'вот', 'ну', 'то', 'же'
}


def normalize_text(text: str) -> str:
    """
    Обработка текста: всё в нижний регистр и исправляет опечатки.
    Например йогурт на ёгурт.

    Пример: normalize_text("текст для обработки")
    """
    text = text.lower()
    # Замена ё на е
    text = text.replace('ё', 'е')
    # Исправления слов
    text = text.replace('звёзды', 'звезды')
    text = text.replace('шёпот', 'шепот')
    text = text.replace('йогурт', 'ёгурт')
    # Дополнительные исправления (можно добавить больше)
    text = text.replace('ёлка', 'елка')
    text = text.replace('мёд', 'мед')
    text = text.replace('лёд', 'лед')
    text = text.replace('характиристики', 'характеристики')

    # Удаляем знаки препинания кроме дефиса
    text = re.sub(r'[^\w\s-]', ' ', text)
    # Удаляем лишние пробелы
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def find_closest_word(word: str) -> str:
    """
    Находит ближайшее слово (исправляет опечатки).
    Пока просто возвращает слово как есть.
    Можно добавить логику исправления опечаток.
    """
    # Простая логика: если слово слишком короткое, возвращаем None
    if len(word) < 2:
        return None

    # Можно добавить словарь для исправления опечаток
    common_typos = {
        'првиет': 'привет',
        'магазин': 'магазин',
        'абазат': 'обязать',
        'кмпьютер': 'компьютер'
    }

    return common_typos.get(word, word)


def extract_keyparola(text: str) -> str:
    """
    Извлекает случайное ключевое слово из текста.
    Вероятность выбора слова пропорциональна его весу.
    """
    # Нормализуем текст и разбиваем на слова
    normalized_text = normalize_text(text)
    words = normalized_text.split()

    keyword_weights = {}

    for word in words:
        # Пропускаем стоп-слова
        if word in STOP_WORDS:
            continue

        # Находим ближайшее слово (исправляем опечатки)
        closest = find_closest_word(word)
        if closest:
            # Вес зависит от позиции слова в предложении и длины
            position_weight = 1.0 if len(words) <= 3 else 0.8
            length_weight = min(len(word) / 10, 1.0)
            weight = position_weight * length_weight

            if closest in keyword_weights:
                keyword_weights[closest] += weight
            else:
                keyword_weights[closest] = weight

    # Если нет ключевых слов, возвращаем пустую строку
    if not keyword_weights:
        return ""

    # Преобразуем в списки для удобной работы
    keywords = list(keyword_weights.keys())
    weights = list(keyword_weights.values())

    # Выбираем случайное слово с вероятностями, пропорциональными весам
    selected_keyword = random.choices(keywords, weights=weights, k=1)[0]

    return selected_keyword


# Дополнительная функция для тестирования
def test_extraction(text: str, n_trials: int = 10):
    """Тестирует функцию extract_keyparola"""
    print(f"Текст: '{text}'")
    print("Результаты 10 запусков:")

    results = {}
    for i in range(n_trials):
        keyword = extract_keyparola(text)
        if keyword:
            results[keyword] = results.get(keyword, 0) + 1

    # Выводим статистику
    for word, count in results.items():
        print(f"  '{word}': {count} раз ({count / n_trials * 100:.1f}%)")
    print()


# Примеры использования
if __name__ == "__main__":
    print("=== Тестирование функций ===")

    # Тест normalize_text
    test_text = "Привет, мир! Йогурт, звёзды и шёпот... Как дела?"
    print(f"Исходный текст: {test_text}")
    print(f"После normalize_text: {normalize_text(test_text)}")
    print()

    # Тест extract_keyparola
    texts_to_test = [
        "Машинное обучение и искусственный интеллект",
        "Красное яблоко и спелый банан",
        "Быстрая коричневая лиса прыгает через ленивую собаку",
        "Погода сегодня хорошая",
        "Йогурт со звёздами и шёпот ветра"
    ]

    for text in texts_to_test:
        test_extraction(text)

    # Одиночный вызов
    keyword = extract_keyparola("Программирование на Python и JavaScript")
    print(f"\nКлючевое слово для 'Программирование на Python и JavaScript': {keyword}")