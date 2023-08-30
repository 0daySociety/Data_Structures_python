def word_frequency(sentence):
    words = sentence.split()
    frequency_dict = {}
    
    for word in words:
        # Remove punctuation and convert to lowercase
        word = word.strip(".,!?").lower()
        
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
    
    print(frequency_dict)



word_frequency("my name is kimeima is")