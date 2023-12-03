import re


def rule_getter(rules):
    """
    Generates a rule catalog from a list of rule-strings in which the directly contained bags of all bags are stored.
    :param rules: list of rules as strings
    :return: rule_catalog: dictionary in the form of {-bag-: [-type_of_bag-, ...], ...}, rule_catalog_n: dictionary in
     form of {-bag-: [[-n_bags-, -type_of_bag-], ...], ...}
    """
    rule_catalog = {}
    rule_catalog_n = {}
    num_pattern = '[0-9]+'
    bag_pattern = '([a-z ]*)bag'
    for rule_raw in rules:
        num_matches = re.findall(num_pattern, rule_raw)
        if len(num_matches) > 0:
            bag_matches = [element.strip() for element in re.findall(bag_pattern, rule_raw)]
        else:
            words = rule_raw.split(' ')
            bag_matches = [words[0] + ' ' + words[1]]
        rule_catalog_n[bag_matches[0]] = [[int(num), bag] for num, bag in zip(num_matches, bag_matches[1:])]
        rule_catalog[bag_matches[0]] = [bag for bag in bag_matches[1:]]

    return rule_catalog, rule_catalog_n


def gold_finder(bag, rule_catalog):
    """
    Searches for any shiny golden within a specified -bag_. Return True if one was found and False if this wasn't the
    case.
    :param bag: type of bag for which it should be checked if it contains a shiny golden bag
    :param rule_catalog: rule_catalog as returned by the function "rule_getter"
    :return: True when a shiny golden bag was found, False in the other case
    """
    if 'shiny gold' in rule_catalog[bag]:
        return True

    elif not rule_catalog[bag]:
        return False

    else:
        for b in rule_catalog[bag]:
            if gold_finder(b, rule_catalog):
                return True
        else:
            return False


def find_num_bags(bag, rule_catalog):
    """
    Finds the total number of bags within a specific -bag-.
    :param bag: type of bag
    :param rule_catalog: rule_catalog_n as returned by the function "rule_getter"
    :return: total number of bags within a -bag-
    """
    if not rule_catalog[bag]:
        return 0
    else:
        result = 0
        for n, b in rule_catalog[bag]:
            result += n + n * find_num_bags(b, rule_catalog)
        return result
