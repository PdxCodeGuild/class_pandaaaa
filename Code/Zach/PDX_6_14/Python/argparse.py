import random
import argparse

import requests


def get_joke_from_api(term=None, page=1):
    """
    Retrieves joke from icanhazdadjoke.com
    :param term: (String) Filters jokes to match search term
    :param page: (String) Page number to use in search
    :return: None
    """
    endpoint = 'https://icanhazdadjoke.com/search'
    params = {'page': page}
    if term:
        params['term'] = term
    headers = {'Accept': 'application/json'}
    response = requests.get(endpoint, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def get_user_input():
    """
    Uses ArgParse to get search term and number of jokes
    :return: Arguments used to start program
    """
    args = argparse.ArgumentParser()
    args.add_argument('-t', '--term', default=None,
                      help="Find a joke containing the term")
    args.add_argument('-n' '--number-of-jokes', dest='number_of_jokes', default=1, type=int,
                      help='Number of jokes you would like to receive')
    return args.parse_args()


def tell_jokes():
    """
    Prints out dad jokes
    :return: None
    """
    args = get_user_input()
    jokes = []
    page = 1
    jokes_per_page = 20
    jokes_json = get_joke_from_api(term=args.term, page=page)
    # Start from a random page if no term is applied and
    if not args.term and args.number_of_jokes <= jokes_per_page:
        page = random.randrange(1, jokes_json['total_pages'] - 1)
        jokes_json = get_joke_from_api(term=args.term, page=page)
    # Validate we have enough jokes to satisfy the request
    validate_joke_criteria(args, jokes_json)
    # Get jokes within the first response in random order
    for i in range(args.number_of_jokes):
        if len(jokes_json['results']) == 0:
            # pull from a new page if we've exhausted all of the jokes from the first page
            page += 1
            jokes_json = get_joke_from_api(term=args.term, page=page)
        new_joke = random.choice(jokes_json['results'])
        jokes.append(new_joke['joke'])
        jokes_json['results'].remove(new_joke)
    print("\n\n".join(jokes))


def validate_joke_criteria(args, jokes_json):
    """
    Validates API contains enough jokes to satisfy request
    :param args: ArgParse arguments
    :param jokes_json: Dictionary containing API response
    :return: None
    """
    if args.term and jokes_json['total_jokes'] < args.number_of_jokes:
        raise Exception(
            f"Was unable to find {args.number_of_jokes} jokes"
            f" that match the search filter: {args.term}"
        )
    if jokes_json['total_jokes'] < args.number_of_jokes:
        raise Exception(
            f"You are requesting {args.number_of_jokes},"
            f" but this API only contains a total of {jokes_json['total_jokes']}"
        )


if __name__ == '__main__':
    tell_jokes()