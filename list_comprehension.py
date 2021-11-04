search_terms = ['the', 'slow', 'green', 'fox']
search_string = "The slow brown fox jumps over the lazy green dog"
if all(search_term in search_string for search_term in search_terms):
    print("Found all terms")
else:
    print("Not all terms found")

