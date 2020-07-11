import requests
from bs4 import BeautifulSoup
import webbrowser

# Requests for top tags in nhentai
tag_rankings_url = "https://nhentai.net/tags/popular"
response = requests.get(tag_rankings_url)
soup = BeautifulSoup(response.text, "html.parser")

# parse from 19 onwards for top 10

nhentai = "https://nhentai.net/search/?q="

include = []
exclude = []

# Explains to user how to use program
print("The program will prompt you first for tags you want to see in your hentai.\n"
      "Next, it will then prompt you for tags you don't want to see in your hentai.\n"
      "You simply type in the tag you want to add/remove from the search.\n"
      "You can type in 'check tags' to see what tags you have added to your include/exclude tag list.\n"
      "Type in 'end' when you are ready to move on.\n")

print("Here are the Top 10 tags on nhentai:")

counter = 19
while counter != 29:
    html = str(soup.findAll('a')[counter])
    array = html.split()
    tag = array[3][11:-8]
    pop_count = array[-1][14:-11]
    counter += 1
    print(f"- {tag.title()} {pop_count}")


# creates include tags
while True:
    print("\nWhat tag do you want to see in your hentai?\n")
    in_tags = input()

    # Formats input
    in_tags = in_tags.lower()
    in_tags = in_tags.rstrip()
    in_tags = in_tags.replace(" ", "-")

    if in_tags == "end":
        break
    elif in_tags == "delete previous":
        print(f"'{include[-1]}' has been removed.")
        include.remove(include[-1])

    elif in_tags == "check tags":
        print("You have the following in your want tags: ")
        for tags in include:
            print(f"+{tags}")
    else:
        include.append(in_tags)
        print(f"Added '{in_tags}'")

# creates exlcude tags
while True:
    print("\nWhat tags do you NOT want to see in your hentai?\n")
    out_tags = input()
    out_tags = out_tags.lower()
    out_tags = out_tags.rstrip()
    out_tags = out_tags.replace(" ", "-")

    if out_tags == "end":
        break
    elif out_tags == "delete previous":
        print(f"'{exclude[-1]}' has been removed.")
        exclude.remove(exclude[-1])

    elif out_tags == "check tags":
        print("You have the following in your unwanted tags: ")
        for tags in exclude:
            print(f"+{tags}")
    else:
        exclude.append(out_tags)
        print(f"Added '{out_tags}'")

include = ["%2B" + i for i in include]
exclude = ['-' + i for i in exclude]

tag_url = "+".join(include + exclude)

website = nhentai + tag_url

webbrowser.open(website)