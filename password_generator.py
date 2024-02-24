import random
import string

# Define character sets for different complexity levels
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

def generate_password(length, complexity):
  """
  Generates a random password based on user-specified length and complexity.

  Args:
    length: Desired length of the password (int).
    complexity: Complexity level (str, "low", "medium", "high").

  Returns:
    Generated password (str).
  """
  char_sets = []
  # Set character sets based on complexity
  if complexity == "low":
    char_sets = [lowercase, digits]
  elif complexity == "medium":
    char_sets = [lowercase, uppercase, digits]
  elif complexity == "high":
    char_sets = [lowercase, uppercase, digits, symbols]
  else:
    raise ValueError("Invalid complexity level. Please choose low, medium, or high.")

  # Combine character sets and pick random characters
  combined_chars = "".join(char_sets)
  password = "".join(random.choice(combined_chars) for _ in range(length))

  return password

def main():
  # Get user input
  while True:
    try:
      length = int(input("Enter desired password length (minimum 8): "))
      if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
      complexity = input("Choose complexity level (low, medium, high): ").lower()
      if complexity not in ["low", "medium", "high"]:
        raise ValueError("Invalid complexity level. Please choose low, medium, or high.")
      break
    except ValueError as e:
      print(e)

  # Generate and display password
  password = generate_password(length, complexity)
  print("Your generated password:", password)

if __name__ == "__main__":
  main()
