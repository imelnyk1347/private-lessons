from work_with_text.find_word_on_text import get_text_from_user
from work_with_text.replace_word_on_text import replace_word_on_text
from work_with_text.counts_words_on_text import counts_word_on_text
from work_with_text.counting_letters_on_text import counting_letters_on_text


def intermediate(choice):
    match choice:
        case 1:
            return get_text_from_user()
        case 2:
            return replace_word_on_text()
        case 3:
            return counts_word_on_text()
        case 4:
            return counting_letters_on_text()
