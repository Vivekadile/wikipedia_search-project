import wikipedia

def get_summary(keyword):
    try:
        results = wikipedia.search(keyword)

        if not results:
            return None, "No results found"

        summary = wikipedia.summary(results[0], sentences=5)
        return summary, None

    except wikipedia.exceptions.DisambiguationError as e:
        return None, f"Too many meanings: {e.options[:5]}"

    except wikipedia.exceptions.PageError:
        return None, "Page not found"

    except Exception as e:
        return None, str(e)