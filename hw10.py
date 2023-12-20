# with open("suallar_copy.txt", "r") as file:
#     text = file.read()

# sentences = text.split('. ') 
# for sentence in sentences:
#     print(sentence)

def count_sentences(text):
    with open("suallar_copy.txt", "r") as file:
        text = file.read()
    sentence_endings = ['.', '!', '?']
    count = 0
    sentences = "--".join(text.split("."))
    sentences = "--".join(sentences.split("!"))
    sentences = "--".join(sentences.split("?"))
    sentences = sentences.split("--") 
    # print(sentences)
    for a in sentences:
        if len(a.replace("#","").strip())>=2:
            print("--- ",a)
            count+=1
            
    print(count)
