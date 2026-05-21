import requests

try:
    response = requests.get('http://localhost:3000/api/books')
    print(f"Status Code: {response.status_code}") # This will tell us if it connected
    
    if response.status_code == 200:
        books = response.json()
        print("Successfully connected!")
        for book in books:
            print(f"- {book['title']} ({book['status']})")
    else:
        print("Failed to connect.")
except Exception as e:
    print(f"An error occurred: {e}")

def calculate_fine(days_borrowed):
    if days_borrowed > 14:
        return (days_borrowed - 14) * 5  # $5 per day after 14 days
    return 0

# Logic to request data, then process it
data = requests.get('http://localhost:3000/api/books').json()
# [Run your fine calculator logic here]