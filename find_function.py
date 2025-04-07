def find_function_in_file(filename, search_string):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        for i, line in enumerate(lines):
            if search_string in line:
                return i + 1  # Adding 1 because line numbers start at 1, not 0
                
        return "Function not found in the file"
            
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    filename = "index.html"
    search_string = "function markTopicAsCompleted"
    
    line_number = find_function_in_file(filename, search_string)
    print(f"The function '{search_string}' is located at line {line_number}") 