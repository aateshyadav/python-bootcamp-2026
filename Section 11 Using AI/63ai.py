""" import re    # with re package

def slugify(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-').lower()

print(slugify("hey you are good"))
# hey-you-are-good

print(slugify("Hello, World!"))
# hello-world

print(slugify("Python & Django @ 2025"))
# python-django-2025

print(slugify("   multiple   spaces   "))
# multiple-spaces """


def slugify(text: str) -> str:     # without re package
    # Store the final characters here
    result = []

    # Track whether the last character added was a dash
    # This prevents multiple consecutive dashes
    prev_dash = False

    # Loop through each character in the input string
    for char in text:

        # Keep letters and numbers
        if char.isalnum():
            result.append(char.lower())  # convert to lowercase
            prev_dash = False

        # Replace spaces/special characters with a single dash
        elif not prev_dash:
            result.append('-')
            prev_dash = True

    # Convert list of characters into a string
    slug = ''.join(result)

    # Remove leading/trailing dashes
    return slug.strip('-')


# Example usage
input_string = "Hello,   World! Python & Django @ 2025"

output = slugify(input_string)

print(output)
# hello-world-python-django-2025
