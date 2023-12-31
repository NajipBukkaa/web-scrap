# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jni7uAqto2PkJ1S9CxJlhHoKCHYrSjip
"""

from googlesearch import search

def search_google_images(query, num_images=5):
    search_results = search(query, num=num_images, stop=num_images, pause=2.0)

    image_links = []
    for result in search_results:
        if result.startswith("https://www.google.com/imgres"):
            # Skip Google's image placeholders
            continue
        image_links.append(result)

    return image_links

if __name__ == "__main__":
    query = "animals"
    num_images = 5

    image_links = search_google_images(query, num_images)

    print(f"Links to {num_images} images of {query}:")
    for i, link in enumerate(image_links, 1):
        print(f"{i}. {link}")