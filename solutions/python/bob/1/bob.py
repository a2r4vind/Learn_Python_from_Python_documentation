def response(hey_bob):
    """Function determines what Bob will reply to someone when they say something to him or ask him a question.

    para: hey_bob: str - statement or question.
    """

    phrase = hey_bob.strip()

    if not phrase:
        return "Fine. Be that way!"

    is_question = phrase.endswith('?')

    is_yelling = phrase.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    if is_question:
        return "Sure."

    if is_yelling:
        return "Whoa, chill out!"

    return "Whatever."
