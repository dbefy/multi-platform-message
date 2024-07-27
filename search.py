def full_text_search(file_name, keyword):
    with open(file_name, 'r') as file:
        text = file.read()
    if keyword in text:
        return f"Keyword '{keyword}' found in the file."
    else:
        return f"Keyword '{keyword}' not found in the file."
    



def facet_search(file_path, facet):
    result = []
    
    with open(file_path, 'r') as file:
        for line in file:
            if facet in line:
                result.append(line.strip())
                
    return result


print(full_text_search("messages.txt", "1"))
print(facet_search("D:\учеба в миигаик\летняя практика\multi platform messages\messages.txt", "1"))
