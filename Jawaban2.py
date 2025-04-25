def analyze_text(text):
    vowels = "aiueoAIUEO"
    vowel_count = 0
    consonant_count = 0
    word_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    words = text.split()
    word_count = len(words)

    return vowel_count, consonant_count, word_count


input_text = input("Masukkan teks: ")
vowel_count, consonant_count, word_count = analyze_text(input_text)

print("Jumlah huruf vokal:", vowel_count)
print("Jumlah huruf konsonan:", consonant_count)
print("Jumlah kata:", word_count)
