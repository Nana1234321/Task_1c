def prefix_function(s):
    n = len(s)
    pi = [0] * n  # Массив для хранения префиксной функции
    max_value = 0  # Переменная для хранения максимального значения

    for i in range(1, n):
        j = pi[i - 1]  
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]  
        if s[i] == s[j]:
            j += 1  
        pi[i] = j  
        max_value = max(max_value, pi[i])  # Обновляем максимальное значение

    return max_value  # Возвращаем  максимальное значение найденное в данной префикс функции

def remove_prefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]  # Отрезаем префикс
    return s  # Если префикс отсутствует, возвращаем строку без изменений


def main():
    word_counts = {}
    word_counts_1 = {}
    new_word_counts = {}
    rewrite_word_counts = {}
    request = ''
    while True:
        command = input("Введите команду text/request : ").strip()
        if command.lower() == "text":
            text = input("Введите слова")
            words = text.split(' ')
            for word in words:
                word = word.strip()  
                if word in word_counts:
                    word_counts[word] += 1
                    new_word = remove_prefix(word, request)
                    if new_word in new_word_counts:
                        new_word_counts[new_word]+=1
                    else:
                        new_word_counts[new_word] = 1
                else:
                    word_counts[word] = 1
                    new_word = remove_prefix(word, request)
                    if new_word in new_word_counts:
                        new_word_counts[new_word]+=1
                    else:
                        new_word_counts[new_word] = 1

            
            print("Словарь:", word_counts)
            #print("Словарь:", new_word_counts)

        elif command.lower() == "request":
            request = input()
            max_count = 0
            new_word_counts.clear()
            for word in word_counts:
                if(prefix_function('#' + request + '#' + word) == len(request) +1):
                    new_word = remove_prefix(word, request)
                    #print(word_counts, word_counts[word])
                    # Создаём ещё один словарь где уже будем хранить для команды дописывание
                    new_word_counts[new_word] = word_counts[word]
                    if(max_count < word_counts[word]):
                        max_count = word_counts[word]
            #print(max)
            try:
                key = next(key for key, value in word_counts.items() if value == max_count)
            except StopIteration:
                key = None

            print(key)

        elif command.lower() == "write":
            ad = input()
            max_count = 0
            rewrite_word_counts.clear()
            for new_word in new_word_counts:
                word = new_word
                rewrite_word_counts[word] = new_word_counts[new_word]
            new_word_counts.clear()
            
            for word in rewrite_word_counts:
                if(prefix_function('#' + ad + '#' + word) == len(ad) + 1):
                    new_word = remove_prefix(word, ad)
                    new_word_counts[new_word] = rewrite_word_counts[word]
                        
                    #print(rewrite_word_counts, rewrite_word_counts[word])
                    if(max_count < rewrite_word_counts[word]):
                        max_count = rewrite_word_counts[word]
            
            try:
                key = next(key for key, value in rewrite_word_counts.items() if value == max_count)
                if request != request + key:
                    print(request+key)
                else:
                    print(request)
                request += ad
            except StopIteration:
                key = None
                
    
        elif command.lower() == "end":
            return 0
        
        else:
            print("Неизвестная команда")
            


if __name__ == "__main__":
    main()
