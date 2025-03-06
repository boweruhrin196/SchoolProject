def random_python_code():
  # Randomly select a programming language
  lang = ["Python", "JavaScript", "Java"]
  lang = random.choice(lang)
  
  # Generate some Python code
  return f"""
  {lang} code:
    
  def main():
    print("Hello, world!")
  
  if __name__ == "__main__":
    main()
"""
