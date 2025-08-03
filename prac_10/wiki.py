import wikipedia


def get_wikipedia_page():
    """Get and display information about a Wikipedia page."""
    search_term = input("Enter page title: ")
    if not search_term:
        return False

    try:
        page = wikipedia.page(search_term, auto_suggest=False)
        print(f"\n{page.title}")
        print(wikipedia.summary(search_term, auto_suggest=False))
        print(page.url)
    except wikipedia.DisambiguationError as e:
        print(f"\nWe need a more specific title. Try one of these:\n{e.options}")
    except wikipedia.PageError:
        print(f"\nPage '{search_term}' does not exist. Try another!")

    return True


def main():
    """Run the Wikipedia search program."""
    print("Wikipedia Search")
    while get_wikipedia_page():
        pass
    print("Thank you.")


if __name__ == "__main__":
    main()